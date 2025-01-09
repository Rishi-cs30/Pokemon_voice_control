Added:
added speech recognition using the speech_recognition library to allow players to issue voice commands.

fuzzy string matching using the fuzzywuzzy library to handle voice command alternatives with up to 80% similarity.

listen() Function: Added a function to capture and process voice inputs via microphone.

match_command() Function: Added functionality to match user input to predefined commands based on similarity thresholds.

Voice Command for Moves: Players can now choose Pokémon moves using voice commands.

Voice Command Options: Allowed players to explore, view Pokémon, battle, or exit using spoken commands.

Removed:
replaced rigid input validation for text-based commands with flexible voice command handling.

Dependency on Only Text Commands: The game no longer relies solely on text-based input; it is now voice-enabled.

Changed:
Input Method: Transitioned from text-only input() prompts to a combination of voice recognition and text prompts as fallback.

Battle Flow: Updated the battle mechanism to accept voice commands for selecting moves.

Menu Navigation: Players can now navigate the game menu using spoken commands instead of typing choices.

Added voice feedback for recognized commands and error handling when commands are misinterpreted.
