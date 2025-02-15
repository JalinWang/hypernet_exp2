import torchvision
import torch.nn as nn

def get_mnet_model(args):
    num_outputs = 10
    device = args.cfg.device

    # if config.cl_scenario == 1 or config.cl_scenario == 3:
    #     num_outputs *= config.num_tasks


    in_shape = [32, 32, 3]
    out_shape = [num_outputs]

    # mnet = ResNet(
    #     in_shape=in_shape, 
    #     num_classes=out_shape[0],
    # ).to(device)

    
    resnet_model = torchvision.models.resnet18(pretrained=True)
    num_ftrs = resnet_model.fc.in_features
    resnet_model.fc = nn.Linear(num_ftrs, num_outputs)
    resnet_model.to(device)

    mnet = resnet_model

    # mnet =  get_mnet_model(config, net_type, in_shape, out_shape, device,
    #                               no_weights=no_weights)

    # init_network_weights(mnet.weights, config, logger, net=mnet)

    return mnet


# def get_mnet_model(config, net_type, in_shape, out_shape, device
#                    no_weights=False):

#     net_act = "relu"
#     no_bias = get_val('no_bias')
#     dropout_rate = get_val('dropout_rate')
#     specnorm = get_val('specnorm')
#     bn_no_running_stats = True
#     bn_distill_stats = False
#     #bn_no_stats_checkpointing = get_val('bn_no_stats_checkpointing')


#     batchnorm = get_val('batchnorm')
#     no_batchnorm = get_val('no_batchnorm')
#     use_batch_norm = True




#     assert(net_type == 'resnet')
#     assert(len(out_shape) == 1)

#     mnet = ResNet(
#         in_shape=in_shape, 
#         num_classes=out_shape[0],
#         verbose=True, #n=5,
#         no_weights=no_weights,
#         use_batch_norm=use_batch_norm,
#         bn_track_stats=bn_no_running_stats,
#         distill_bn_stats=bn_distill_stats,
#     ).to(device)


#     return mnet



# def str_to_act(act_str):
#     """Convert the name of an activation function into the actual PyTorch
#     activation function.

#     Args:
#         act_str: Name of activation function (as defined by command-line
#             arguments).

#     Returns:
#         Torch activation function instance or ``None``, if ``linear`` is given.
#     """
#     if act_str == 'linear':
#         act = None
#     elif act_str == 'sigmoid':
#         act = torch.nn.Sigmoid()
#     elif act_str == 'relu':
#         act = torch.nn.ReLU()
#     elif act_str == 'elu':
#         act = torch.nn.ELU()
#     else:
#         raise Exception('Activation function %s unknown.' % act_str)
#     return act
