#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/range.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "geometry_msgs/msg/pose.hpp"
#include <tf2/LinearMath/Quaternion.h>
#include <tf2/LinearMath/Matrix3x3.h>


class GotoGoal : public rclcpp::Node
{
public:
    GotoGoal() : Node("go_to_goal_node")
    {
        this->declare_parameter<double>("set_point_x" , 5.0);
        this->declare_parameter<double>("set_point_y" , 5.0);
        this->declare_parameter<double>("set_point_z" , 5.0);
        this->declare_parameter<double>("kp_angle" , 0.5);
        this->declare_parameter<double>("kp_distance" , 0.5);
        pose_subscriber = this->create_subscription<geometry_msgs::msg::Pose>(
            "/drone/gt_pose", 10, std::bind(&GotoGoal::pose_callback, this, std::placeholders::_1));

        sonar_subscriber = this->create_subscription<sensor_msgs::msg::Range>(
            "/drone/sonar", 10, std::bind(&GotoGoal::sonar_callback, this, std::placeholders::_1));

        cmd_vel_publisher = this->create_publisher<geometry_msgs::msg::Twist>("/drone/cmd_vel", 10);
        RCLCPP_INFO(this->get_logger(), "------ GTG Node Started -----");
    }



private:

double get_yaw_from_quaternion(const geometry_msgs::msg::Quaternion &quat) {
    tf2::Quaternion q(quat.x, quat.y, quat.z, quat.w);
    tf2::Matrix3x3 m(q);
    double roll, pitch, yaw;
    m.getRPY(roll, pitch, yaw);
    return yaw;
  }
    void sonar_callback(const sensor_msgs::msg::Range::SharedPtr camera_msg)
    {
        double goal_x=this->get_parameter("set_point_x").as_double();
        double goal_y=this->get_parameter("set_point_y").as_double();
        double goal_z=this->get_parameter("set_point_z").as_double();
        double kp_angle=this->get_parameter("kp_angle").as_double();
        double kp_distance=this->get_parameter("kp_distance").as_double();


        double error_x = goal_x - current_pose.position.x;
        double error_y = goal_y - current_pose.position.y;
        double error_z = goal_z - current_pose.position.z;
        double yaw = get_yaw_from_quaternion(current_pose.orientation);
        //  Ecludian Distance EQ

        double error_in_distance = sqrt(pow(error_x, 2) + pow(error_y, 2));
        double error_in_angle = atan2(error_y, error_x) - yaw;
        error_in_angle = atan2(sin(error_in_angle), cos(error_in_angle));

        error_in_distance = std::max(0.0 , std::min(error_in_distance,1.0));
        error_in_angle = std::max(-1.0 , std::min(error_in_angle,1.0));
        error_z = std::max(-1.0, std::min(error_z,10.0));



        RCLCPP_INFO(this->get_logger(), "E_D : %f  - E_A : %f ", error_in_distance,error_in_angle);


        if(error_in_distance > 0.2 || fabs(error_z) > 0.3){
            velocity_msg.linear.x = kp_distance * error_in_distance;
            velocity_msg.linear.z = error_z;
            velocity_msg.angular.z = kp_angle * error_in_angle;

        }else {

            velocity_msg.linear.x = 0.0;
            velocity_msg.angular.z = 0.0;
            velocity_msg.linear.z = 0.0;

        }
        cmd_vel_publisher->publish(velocity_msg);

    }

    void pose_callback(const geometry_msgs::msg::Pose::SharedPtr pose_msg)
    {
        current_pose = *pose_msg;
    }

    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr cmd_vel_publisher;
    rclcpp::Subscription<sensor_msgs::msg::Range>::SharedPtr sonar_subscriber;
    rclcpp::Subscription<geometry_msgs::msg::Pose>::SharedPtr pose_subscriber;
    geometry_msgs::msg::Pose current_pose;
    geometry_msgs::msg::Twist velocity_msg;

};


int main(int argc, char ** argv)
{


    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<GotoGoal>());
    rclcpp::shutdown();
    return 0;
}