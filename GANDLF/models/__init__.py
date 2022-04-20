from .unet import unet, resunet
from .light_unet import light_unet, light_resunet
from .unet_multilayer import unet_multilayer, resunet_multilayer
from .light_unet_multilayer import light_unet_multilayer, light_resunet_multilayer
from .deep_unet import deep_unet, deep_resunet
from .uinc import uinc
from .fcn import fcn
from .vgg import vgg11, vgg13, vgg16, vgg19
from .densenet import densenet121, densenet169, densenet201, densenet264
from .resnet import resnet18, resnet34, resnet50, resnet101, resnet152
from .efficientnet import (
    efficientnetB0,
    efficientnetB1,
    efficientnetB2,
    efficientnetB3,
    efficientnetB4,
    efficientnetB5,
    efficientnetB6,
    efficientnetB7,
)
from .imagenet_vgg import (
    imagenet_vgg11,
    imagenet_vgg11_bn,
    imagenet_vgg13,
    imagenet_vgg13_bn,
    imagenet_vgg16,
    imagenet_vgg16_bn,
    imagenet_vgg19,
    imagenet_vgg19_bn,
)
from .sdnet import SDNet
from .MSDNet import MSDNet
from .brain_age import brainage
from .unetr import unetr

# defining dict for models - key is the string and the value is the transform object
global_models_dict = {
    "unet": unet,
    "unet_multilayer": unet_multilayer,
    "resunet": resunet,
    "resunet_multilayer": resunet_multilayer,
    "residualunet": resunet,
    "residualunet_multilayer": resunet_multilayer,
    "deepunet": deep_unet,
    "lightunet": light_unet,
    "lightunet_multilayer": light_unet_multilayer,
    "deep_unet": deep_unet,
    "light_unet": light_unet,
    "light_unet_multilayer": light_unet_multilayer,
    "deepresunet": deep_resunet,
    "lightresunet": light_resunet,
    "lightresunet_multilayer": light_resunet_multilayer,
    "deep_resunet": deep_resunet,
    "light_resunet": light_resunet,
    "light_resunet_multilayer": light_resunet_multilayer,
    "unetr": unetr,
    "fcn": fcn,
    "uinc": uinc,
    "vgg": vgg19,
    "vgg11": vgg11,
    "vgg13": vgg13,
    "vgg16": vgg16,
    "vgg19": vgg19,
    "imagenet_vgg11": imagenet_vgg11,
    "imagenet_vgg11_bn": imagenet_vgg11_bn,
    "imagenet_vgg13": imagenet_vgg13,
    "imagenet_vgg13_bn": imagenet_vgg13_bn,
    "imagenet_vgg16": imagenet_vgg16,
    "imagenet_vgg16_bn": imagenet_vgg16_bn,
    "imagenet_vgg19": imagenet_vgg19,
    "imagenet_vgg19_bn": imagenet_vgg19_bn,
    "densenet": densenet264,
    "densenet121": densenet121,
    "densenet169": densenet169,
    "densenet201": densenet201,
    "densenet264": densenet264,
    "msdnet": MSDNet,
    "brain_age": brainage,
    "sdnet": SDNet,
    "resnet18": resnet18,
    "resnet34": resnet34,
    "resnet50": resnet50,
    "resnet101": resnet101,
    "resnet152": resnet152,
    "efficientnetb0": efficientnetB0,
    "efficientnetb1": efficientnetB1,
    "efficientnetb2": efficientnetB2,
    "efficientnetb3": efficientnetB3,
    "efficientnetb4": efficientnetB4,
    "efficientnetb5": efficientnetB5,
    "efficientnetb6": efficientnetB6,
    "efficientnetb7": efficientnetB7,
}


def get_modelbase_final_layer(final_convolution_layer):
    """
    This function gets the final layer of the model.

    Args:
        final_convolution_layer (str): The final layer of the model as a string.

    Returns:
        Functional: sigmoid, softmax, or None
    """
    none_list = [
        "none",
        None,
        "None",
        "regression",
        "classification_but_not_softmax",
        "logits",
        "classification_without_softmax",
    ]

    if final_convolution_layer in ["sigmoid", "sig"]:
        final_convolution_layer = torch.sigmoid

    elif final_convolution_layer in ["softmax", "soft"]:
        final_convolution_layer = F.softmax

    elif final_convolution_layer in none_list:
        final_convolution_layer = None

    return final_convolution_layer
