from injector import Module, provider, singleton, Injector
from .gladiator_interface import GladiatorInterface
from .gladiator_service import GladiatorService


class GladiatorModule(Module):

    @singleton
    @provider
    def provide_gladiator(self) -> GladiatorInterface:
        return GladiatorService()


injector = Injector([GladiatorModule()])
