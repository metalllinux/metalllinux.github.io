---
title: "How to Install Grip Mode on Emacs to Preview Markdown Files Like that Seen on GitHub"
category: "editors-and-tools"
tags: ["editors-and-tools", "install", "grip", "mode", "emacs"]
---

# How to Install Grip Mode on Emacs to Preview Markdown Files Like that Seen on GitHub

* Install `python3-pip`:

```
sudo dnf install python3-pip
```

* Install `grip`:

```
pip3 install --user grip
```

* Add the following to `~/.config/doom/init.el`:

```
:lang                                                                                                              
(markdown +grip)                                                                                                   
```

* Run `doom sync`:

```
doom sync
```

* Restart Emacs.

* How to use `grip-mode`:

```
  ┌────────────────────────┬────────────┬────────────────────────────────┐                                           
  │        Command         │ Keybinding │          Description           │                                           
  ├────────────────────────┼────────────┼────────────────────────────────┤                                           
  │ grip-mode              │ SPC m p    │ Toggle live preview in browser │                                           
  ├────────────────────────┼────────────┼────────────────────────────────┤                                           
  │ M-x grip-start-preview │ -          │ Start preview manually         │                                           
  ├────────────────────────┼────────────┼────────────────────────────────┤                                           
  │ M-x grip-stop-preview  │ -          │ Stop preview server            │                                           
  └────────────────────────┴────────────┴────────────────────────────────┘                                           
```

The preview opens at http://localhost:6419 by default.                                                             
                                                                                                                     
Optional: GitHub Token for Higher Rate Limits                                                                      
                                                                                                                     
GitHub's API has rate limits for unauthenticated requests. To increase limits:                                     
                                                                                                                     
1. Create a GitHub personal access token (no scopes needed)                                                        
2. Add to ~/.config/doom/config.el:                                                                                
                                                                                                                     
(setq grip-github-user "your-username")                                                                            
(setq grip-github-password "your-token") 
