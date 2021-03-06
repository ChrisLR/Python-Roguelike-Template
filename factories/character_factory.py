from bodies import body_listing
from characters.character import Character
from components.display import Display
from components.effects import Effects
from components.health import Health
from components.inventory import Inventory
from data.python_templates.characters import character_templates
from data.python_templates.classes import character_class_templates


class CharacterFactory(object):
    """
    At first this will only instantiate templates but eventually it should be able
    to pump out variations of a template ex: Adjusted to match player level.
    """
    def __init__(self, factory_service):
        self.template_instance_count = {}
        self.factory_service = factory_service

    def build(self, uid):
        """
        Builds a characters instance from a template using the uid.
        :param uid: uid of the template to instantiate.
        :return: Built instance from template.
        """

        character_template = character_templates[uid]
        if character_template:
            return self._create_instance_of_template(character_template)
        else:
            raise Exception("Could not find template for UID " + uid)

    def create(self, uid, name, class_uid, race, stats, body_uid, enforce_max_hp=False):
        """
        Creates a new character based on arguments
        :return:
        """
        new_instance = Character(
            uid=uid,
            name=name,
            character_class=self.get_class_template_by_uid(class_uid).copy(),
            character_race=race,
            stats=stats,
            display=Display((255, 255, 255), (0, 0, 0), "@"),
            # TODO This is temporary, we will change this with a race refactor.
            body=next((body for body in body_listing if body.uid == body_uid))(),
            inventory=Inventory(),
            health=Health(enforce_max_hp),
        )
        new_instance.register_component(Effects())

        return new_instance

    def _create_instance_of_template(self, character_template):
        instance_id = 0
        if character_template.uid in self.template_instance_count:
            instance_id = self.template_instance_count[character_template.uid]
            self.template_instance_count[character_template.uid] += 1
        else:
            self.template_instance_count[character_template.uid] = 1

        instance_uid = character_template.uid + "_" + str(instance_id)
        new_instance = character_template.copy()
        new_instance.uid = instance_uid

        return new_instance

    def get_class_template_by_uid(self, uid):
        if uid in character_class_templates:
            return character_class_templates[uid]
