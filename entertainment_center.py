import media
import fresh_tomatoes

#Movie Avatar
avatar=media.Movie("Avatar", 
	"http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp", 
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

#Movie Pacific Rim
pacific_rim=media.Movie("Pacific Rim", 
	"http://t3.gstatic.com/images?q=tbn:ANd9GcSKn2M2lvhByicODxnf-BpZo39agSfgylHjkP498i81bp61eLU-", 
	"https://www.youtube.com/watch?v=_EhiLLOhVis")

#Movie Rampage
rampage=media.Movie("Rampage", 
	"http://t1.gstatic.com/images?q=tbn:ANd9GcQpTCKCvU_Fz0SwP_oyuSSKdf_unn88WWa5evQC4F3U7EfHyQVJ", 
	"https://www.youtube.com/watch?v=coOKvrsmQiI")

#Movie Rang De Basanti
rang_de_basanti=media.Movie("Rang De Basanti", 
	"http://media.glamsham.com/download/wallpaper/movies/images/r/rangdebasanti1_10x7.jpg", 
	"https://www.youtube.com/watch?v=l-BTOTtcGmk")

#Movie Raid
raid=media.Movie("Raid", 
	"http://t0.gstatic.com/images?q=tbn:ANd9GcRMkJGUfownu2pK7Ym7PTWhU8flMg9P9aT5r7fLUnyXflfYgzSe", 
	"https://www.youtube.com/watch?v=3h4thS-Hcrk")

#Movie Beyond the Clouds
beyond_the_clouds=media.Movie("Beyond the Clouds", 
	"http://t1.gstatic.com/images?q=tbn:ANd9GcRwjyvOLpl2dr7eQGzRyQ89c3YHAcdf8-QIII571983u6DR68w-", 
	"https://www.youtube.com/watch?v=J-IzGBU344M")

#Movie Dark Wind
dark_wind=media.Movie("Beyond the Clouds", 
	"https://upload.wikimedia.org/wikipedia/en/b/b3/Kadvi_Hawa_-_Poster.jpg", 
	"https://www.youtube.com/watch?v=AjKsJfWxtsk")

#Movie Solo
solo=media.Movie("Solo", 
	"http://t2.gstatic.com/images?q=tbn:ANd9GcRvl3Dm7P7F6hRHmpiEF3oR5txrfUDc5Grt9RspFekcd4yS4Gzk", 
	"https://www.youtube.com/watch?v=dNW0B0HsvVs")

fresh_tomatoes.open_movies_page([avatar, pacific_rim, rampage, rang_de_basanti, raid, beyond_the_clouds, dark_wind, solo])
