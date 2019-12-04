from julia import Yao

def apply(register, block):
    """apply a quantum block to the register.
    This is the same with `apply_b`, or `apply!`
    in Julia.
    """
    return Yao.apply_b(register, block)
