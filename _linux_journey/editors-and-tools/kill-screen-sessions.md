---
title: "Kill Screen Sessions"
category: "editors-and-tools"
tags: ["editors-and-tools", "kill", "screen", "sessions"]
---

First, let’s create a couple of sessions to kill:

% screen -dmS my_session_4
% screen -dmS my_session_5

Our two sessions are now created:

% screen -list
There are screens on:
	19665.my_session_4	(Detached)
	19671.my_session_5	(Detached)

We can now use the screen command argument -X to send a command to a running screen session. The -S will allow us to specify the session that will receive the command. So, to send a quit command to my_session_4, we would use:

% screen -S my_session_4 -X quit

The screen -list shows our current sessions:

% screen -list
There is a screen on:
	19671.my_session_5	(Detached)

Lastly, we can always kill a screen session via OS commands. The numbers prepending the name are the PID of the screen session. To kill our last session, we can use kill:

kill 19671