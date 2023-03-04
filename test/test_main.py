from RouteControl import RouteController
from test_case import case1, case2

# test controller initialize
test_controller = RouteController(**case1['routes'])

# test get_instructiion

test_control_list = test_controller.get_instruction(
    status_list=case1['status'],
    loc_list=case1['loc'],
    step_list=case1['step'])

# test update_routes
test_controller.update_routes(**case2)
