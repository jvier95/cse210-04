class Director:


    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._game_score = 0
        
    def start_game(self, cast):
        
        self._video_service.openWindow()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        
        score = cast.get_first_actor("scores")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
            if robot.get_position().equals(artifact.get_position()):                
                if artifact.get_text() == "*":
                    self._game_score =  self._game_score + artifact.get_points()
                else:
                    self._game_score = self._game_score - artifact.get_points()
                score.set_text(f"Score: {self._game_score}")                
                cast.reset_actor(artifact)
            if artifact.get_position().get_y() >= max_y:
                cast.reset_actor(artifact)
        
    def _do_outputs(self, cast):
        
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()