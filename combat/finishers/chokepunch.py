from combat import attacks
from combat.finishers.base import Finisher
from echo import functions
from util import gridhelpers


class ChokePunch(Finisher):
    name = "Choke Punch"
    description = "Choke your enemy as you punch him repeatedly."
    attacker_message = "You grab {defender_his} throat with your hand as you punch {defender_him} " \
                       "repeatedly until {defender_his} face is a bloody pulp."

    observer_message = "{attacker} grabs {defender_his} throat with {attacker_his} hand as {attacker_he} " \
                       "punches {defender_him} repeatedly until {defender_his} face is a bloody pulp."

    @classmethod
    def evaluate(cls, attack_result):
        if attack_result.context.distance_to <= 1:
            if attack_result.context.attack_used == attacks.Punch:
                return True
        return False

    @classmethod
    def execute(cls, attack_result):
        return cls.get_message(attack_result)

    @classmethod
    def get_message(cls, attack_result):
        defender = attack_result.context.defender
        if attack_result.context.attacker.is_player:
            return cls.attacker_message.format(
                defender_his=functions.his_her_it(defender),
                defender_him=functions.him_her_it(defender),
            )
        else:
            return cls.observer_message.format(
                attacker=functions.get_name_or_string(attack_result.context.attacker),
                defender_his=functions.his_her_it(defender),
                attacker_his=functions.his_her_it(attack_result.context.attacker),
                attacker_he=functions.he_her_it(attack_result.context.attacker),
                defender_him=functions.him_her_it(defender)
            )
