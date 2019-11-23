# snippets
Various code snippets

They are typically meant for auto-generating things, such as in `Tagged_WordCount.py` and `wordlist_script.py` so the user only has to run it.


1. gettime.js
   1. For use in Google Sheets 
   2. Input two locations, and get out a time exactly in minutes
   3. One issue:
      1. If trying to apply the formula ie `=GETTIME(B2, admin!B4, "DRIVING")`... When dragging it down and trying to keep the admin one constant, it still doesn't keep constant
      2. So instead I put the option for location2 == "WORK" or "SOCIAL"
2. Tagged_WordCount.py
3. wordlist_script.py
