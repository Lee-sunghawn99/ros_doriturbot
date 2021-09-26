# UTF-8.







import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
PI = 3.14159265359




def move_base_to(x, y, z, w):
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    while (not client.wait_for_server(rospy.Duration(5))):
        rospy.loginfo("Waiting for the move_base action server to come up")

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"

    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    rospy.loginfo("Sending goal")
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available")
    else:
        return client.get_result()



if __name__ == '__main__':
    goal_positions_x = [-0.0390443902218, 0.356677586588, 0.837577197767, 1.26838478976]
    goal_positions_y = [0.136269195672, 1.57275401241, 0.305271469299, 1.98035276588]

    goal_pose_z = [0.77939165152, 0.000488027945771, -0.0149111852193,0.702819391485]
    goal_pose_w = [0.626537032856, 0.999999880914, 0.999888822097, 0.711368331424]

    rospy.init_node("set_navigation_goal")

    for x, y, z, w in zip(goal_positions_x, goal_positions_y, goal_pose_z, goal_pose_w):
        result = move_base_to(x, y, z, w)
        if result:
            continue
        elif not result:
            continue
        else:
            break
        rospy.logininfo("Good job!!!")







