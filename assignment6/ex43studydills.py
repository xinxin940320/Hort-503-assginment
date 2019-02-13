from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):

    last_words = [
                 "You died because you are not smart enough.",
                 "But that is OK.",
                 "You could do better next time."
                 ]


    def enter(self):
        print(Death.last_words[randint(0, len(self.last_words)-1)])
        exit(1)

class LittleCabin(Scene):

    def enter(self):
        print(dedent("""
               You are traveling through the forest.
               You kind of get lost in the forest.
               There is a little cabin showing up."""))

        action = input(">> ")
    if action == "open the door":
        print(dedent("""
              There is a monster hiding behind the door. Once you come inside,
              the monster eats you."""))
        return 'death'

    elif action == "run away":
        print(dedent("""
              You just choose the right choice!
              You run to the left side and then you see a witch standing here.
              She is holding an apple."""))
    else:
        print("DOES NOT COMPUTE!")
        return 'little_cabin'

class PoisonedApple(Scene):

    def enter(self):

        print(dedent("""
        You are thinking about whether eat this apple or not."""))
        action = input(">> ")
        if action == "eat it":
            print(dedent("""
            After a lot of pain,
            you finally find that apple is poisoned."""))
        return 'death'
        #elif:
        #print(dedent(""" You make the good choice."""))
        #return 'escape_way'


class EscapeWay(Scene):

    def enter(self):
        print(dedent("""
        You keep running in the forest, and you see two ways.
        Which way you gonna choose, left or right?"""))
        action = input(">> ")
        if action == "left":
            print(dedent("""
            Congrats! you just win!"""))
        elif action == "right":
            return 'death'



class Map(object):
    scenes = {
         'little_cabin': LittleCabin(),
         'poisoned_apple': PoisonedApple(),
         'escape_way': EscapeWay(),
         'death': Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('little_cabin')
a_game = Engine(a_map)
a_game.play()
