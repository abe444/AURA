# AURA
![screenie](https://github.com/abe444/AURA/assets/105024329/fbaf06e8-70df-4b29-a7e3-6120da555a1d)
A dead simple RSS reader.
- Suckless. ✅
- Written in PYTHON. 🤮 ✅ 
- Meant to be used in conjunction with other GNU userland tools (pairs very well with bash aliases). 

### Syntax:
```
python3 main.py <rss_feed_url> [num_feeds]
```

### Example (.bashrc):
```
alias hackernews='python3 ~/AURA/main.py https://feeds.feedburner.com/TheHackersNews 5'
alias phoronix='python3 ~/AURA/main.py https://www.phoronix.com/rss.php 5'
```

