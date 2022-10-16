import random
from Game.shared.point import Point


class Cast:
   #the actors!
    def __init__(self, cols, rows, cell_size):
        """Constructs a new Actor."""
        self._actors = {}
        self._cols = cols
        self._rows = rows
        self._cell_size = cell_size
        
    def add_actor(self, group, actor):
        
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        """Gets the actors in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The actors in the group.
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy() 
        return results
    
    def get_all_actors(self):
        """Gets all of the actors in the cast.
        
        Returns:
            List: All of the actors in the cast.
        """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_first_actor(self, group):
        
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    def remove_actor(self, group, actor):
        
        if group in self._actors:
            self._actors[group].remove(actor)

    def reset_actor(self, actor):
        x = random.randint(1, self._cols - 1)
        y = random.randint(1, self._rows - 1)
        position = Point(x, y)
        position = position.scale(self._cell_size)
        actor.set_position(position)