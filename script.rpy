################################################################################
# Part 1: 角色、圖片與背景宣告 (Definitions)
################################################################################

# --- 角色宣告 ---
define g1 = Character("林語夏", color="#eabcde")
define g2 = Character("林曉", color="#c081e0")
define b1 = Character("陸景澤", color="#4d53c6")
define b2 = Character("洛星淮", color="#cacbcd")

# --- 圖片定義 (請將對應檔名的圖片放入 images 資料夾) ---

# 林語夏 (g1)
image g1_uniform = "g1_uniform.png"
image g1_casual = "g1_casual.png"
image g1_swimsuit = "g1_swimsuit.png"

# 林曉 (g2)
image g2_uniform = "g2_uniform.png"
image g2_casual = "g2_casual.png"
image g2_swimsuit = "g2_swimsuit.png"
image g2_dance = "g2_dance.png"

# 陸景澤 (b1)
image b1_uniform = "b1_uniform.png"
image b1_basketball = "b1_basketball.png"
image b1_casual = "b1_casual.png"
image b1_swimsuit = "b1_swimsuit.png"

# 洛星淮 (b2)
image b2_uniform = "b2_uniform.png"
image b2_casual = "b2_casual.png"
image b2_swimsuit = "b2_swimsuit.png"
image b2_esports = "b2_esports.png"

# --- 精準位置定義 (Positions) ---
# ***修改點：將 zoom 統一改為 yzoom 來確保所有角色高度一致***
# yzoom 0.85 代表角色高度為螢幕的85%，您可以依喜好調整此數值 (例如 0.8 或 0.9)
# yalign 1.0 確保所有立繪的底部都與螢幕底部貼齊

transform pos_center:
    xalign 0.5 yalign 1.0 yzoom 0.85

# 兩人站位 (g1永遠在左)
transform pos_left:
    xalign 0.25 yalign 1.0 yzoom 0.85
transform pos_right:
    xalign 0.75 yalign 1.0 yzoom 0.85

# 三人站位
transform pos_t_left:
    xalign 0.2 yalign 1.0 yzoom 0.85
transform pos_t_center:
    xalign 0.5 yalign 1.0 yzoom 0.85
transform pos_t_right:
    xalign 0.8 yalign 1.0 yzoom 0.85

# 四人站位 (左右平均分配)
transform pos_farleft:
    xalign 0.12 yalign 1.0 yzoom 0.85
transform pos_leftcenter:
    xalign 0.37 yalign 1.0 yzoom 0.85
transform pos_rightcenter:
    xalign 0.62 yalign 1.0 yzoom 0.85
transform pos_farright:
    xalign 0.87 yalign 1.0 yzoom 0.85

# --- 背景宣告 ---
# 校園篇
image bg room = "bg_room.png"
image bg classroom = "bg_classroom.png"
image bg cafe = "bg_cafe.png"
image bg library = "bg_library.png"
image bg student_council_room = "bg_student_council_room.png"
image bg computer_lab = "bg_computer_lab.png"
image bg sports_field = "bg_sports_field.png"
image bg basketball_court = "bg_basketball_court.png"
image bg esports_cafe = "bg_esports_cafe.png"
image bg esports_arena = "bg_esports_arena.png"
image bg suspension_bridge = "bg_suspension_bridge.png"
image bg airplane = "bg_airplane.png"
# 海灘篇
image bg beach_day = "bg_beach_day.png"
image bg beach_sunset = "bg_beach_sunset.png"
image bg beach_night = "bg_beach_night.png"


################################################################################
# Part 2: 變數初始化 (Variable Initialization)
################################################################################

# --- 校園篇變數 ---
default linxiao_points = 0
default lujingze_points = 0
default luoxinghuai_points = 0

# --- 夏日海灘篇變數 ---
default beach_linxiao_points = 0
default beach_lujingze_points = 0
default beach_luoxinghuai_points = 0


################################################################################
# Part 3: 遊戲腳本本體 (Game Script)
################################################################################

label start:
    "夏日的風，吹來了不同的旋律。"
    "一本未完成的筆記，將從哪一頁開始記錄呢？"

    menu:
        "開始《校園篇》的故事。":
            jump school_chapter
        "開始《夏日海灘篇》的故事。":
            jump beach_chapter

################################################################################
# --- 《校園篇》完整故事線 ---
################################################################################
label school_chapter:
    scene bg room with fade
    "某天清晨"
    "嗡嗡嗡...嗡嗡嗡..."
    "(拿起手機)"
    show g1_uniform at pos_center
    g1 "嗯...起了起了"
    g1 "今天是個好天氣呢"
    g1 "走走走，上學去~"
    hide g1_uniform with dissolve
    
    scene bg classroom with dissolve
    "一天的課程在忙碌中悄然度過。"
    jump day_1_lunch

# --- 週一・午休 | 午餐的邀約 (個人劇情) ---
label day_1_lunch:
    "噹——噹——噹——"
    "午休的鐘聲響起，我趴在桌上，肚子不爭氣地叫了起來。"
    show g1_uniform at pos_rightcenter
    g1 "（好餓...午餐該怎麼解決呢？"
    
    show g2_uniform at pos_leftcenter
    show b2_uniform at pos_farright
    show b1_uniform at pos_farleft
    
    g2 "語夏，我們去福利社吧！聽說今天有賣限定版的日式炒麵麵包！晚了就沒了！"
    b2 "人應該會很多...我想留在教室吃自己帶的便當，比較安靜。"
    b1 "圖書館今天有新書上架。"
    g1 "（午休時間...該和誰一起度過呢？）"

    menu:
        "和林曉一起去福利社湊熱鬧。":
            hide b1_uniform
            hide b2_uniform
            g1 "好啊！為了限定版炒麵麵包，我們要用跑的！"
            g2 "就是要有這種氣勢！"
            $ linxiao_points += 1
            jump day_1_afterschool

        "留在教室，和洛星淮一起安靜地吃午餐。":
            hide b1_uniform
            hide g2_uniform
            g1 "我今天也帶了便當，就不去人擠人了，留在教室吃吧。"
            b2 "妳帶的菜色...看起來很營養均衡，配色也很漂亮。"
            g1 "哈哈，都是我媽媽的愛心。你帶的看起來也很清爽呢。"
            $ luoxinghuai_points += 1
            jump day_1_afterschool

        "去圖書館，希望能遇到陸景澤學長。":
            hide g2_uniform
            hide b2_uniform
            g1 "（去圖書館碰碰運氣好了。）"
            $ lujingze_points += 1
            jump day_1_afterschool

# --- 週一・放學後 | 咖啡廳的閒聊 (團體劇情) ---
label day_1_afterschool:
    scene bg cafe with fade
    "放學後，為了討論報告，我們四個人約在了學校附近的咖啡廳。"
    
    show g1_uniform at pos_rightcenter
    show g2_uniform at pos_leftcenter
    show b1_uniform at pos_farleft
    show b2_uniform at pos_farright

    g2 "這家的鬆餅也太好吃了吧！語夏妳快嚐嚐！"
    g1 "嗯...好好吃！不過...唉...這個報告的封面，我怎麼畫都覺得不對勁。"
    menu:
        "把畫冊推到陸景澤面前。":
            $ lujingze_points += 2
            $ linxiao_points -= 1
            g1 "學長，你覺得這個構圖怎麼樣？給我點建議吧。"
            b1 "重心偏左，視覺上不穩定。配色超過三種主要顏色，顯得雜亂。回去把基礎構圖學好，重畫。"
            g1 "嗚...還是一樣的直接呢。"

        "和洛星淮一起討論色彩搭配。":
            $ luoxinghuai_points += 2
            $ lujingze_points -= 1
            $ linxiao_points -= 1
            g1 "洛同學，你覺得...這裡用暖色調還是冷色調比較好？"
            b2 "嗯...如果主題是『夏日筆記』的話，我覺得可以大膽地試試高飽和的對比色..."

        "乾脆地把畫冊蓋上，和林曉一起吃點心。":
            $ linxiao_points += 2
            $ lujingze_points -= 2
            $ luoxinghuai_points -= 1
            g1 "啊，不想了！越想越煩！我也要吃東西！曉曉，妳的提拉米蘇分我一口！"
            g2 "欸嘿嘿，早就等妳這句話了！來，啊——"
    "愉快的（或緊張的）討論時光很快就過去了。"
    jump day_2_lunch

# --- 週二・午休 | 社團的抉擇 (個人劇情) ---
label day_2_lunch:
    scene bg classroom with fade
    "週二下午是社團時間，我暫時還沒有加入任何社團，正在猶豫。"
    "午休時，三個人分別向我發出了邀請。"
    
    show g1_uniform at pos_rightcenter
    show g2_uniform at pos_leftcenter
    show b1_uniform at pos_farleft
    show b2_uniform at pos_farright

    g2 "語夏！等等來我們熱舞社體驗看看嘛！很好玩的！保證妳會愛上！"
    b1 "學生會缺人手幫忙整理文化祭的資料，妳有空的話就過來。"
    b2 "那個...我的社團在電腦教室...如果妳對遊戲製作有興趣的話，可以來看看..."
    g1 "（三種完全不同的風格...該去哪裡看看呢？）"
    
    menu:
        "答應林曉，去操場看她們跳舞。":
            jump day_2_event_linxiao
        "答應陸景澤，去學生會辦公室幫忙。":
            jump day_2_event_lujingze
        "答應洛星淮，去電腦教室一探究竟。":
            jump day_2_event_luoxinghuai

# --- 週二・放學後 | 個人專屬事件 ---
label day_2_event_linxiao:
    scene bg sports_field with fade
    "下午，我來到操場，熱情的音樂和整齊的口號聲遠遠傳來。"
    show g2_dance at pos_right
    "林曉穿著輕便的舞蹈服，和熱舞社的社員們正在練習，充滿了青春的活力。"
    "一曲結束，她滿頭大汗地向我跑來，眼睛閃閃發亮。"
    show g1_uniform at pos_left
    g2 "呼...呼...語夏，妳覺得怎麼樣？要不要一起來跳？"
    menu:
        "「好啊！看起來很有趣！」":
            $ linxiao_points += 2
            g2 "太好了！來，我教妳最簡單的動作！"
            "雖然我跳得笨手笨腳，但和曉曉一起流汗的感覺非常開心。"
        "「我就不用了，在旁邊幫妳加油就好。」":
            $ linxiao_points += 1
            g1 "妳跳得超棒的！我就在旁邊幫妳加油打氣！"
            "我遞上毛巾和水，曉曉的臉上露出了燦爛的笑容，接過水時手指不經意地碰到了我的。"
    jump day_3_lunch

label day_2_event_lujingze:
    scene bg student_council_room with fade
    "我來到學生會辦公室，裡面安靜得只聽得到空調的聲音。"
    show b1_uniform at pos_right
    b1 "把這些按年份分類就行。"
    show g1_uniform at pos_left
    "整理到一半，我發現了一本舊的相簿。"
    g1 "學長，這是...？"
    b1 "去年的活動紀錄。別看了，快點做事。"
    menu:
        "偷偷翻開相簿。":
            $ lujingze_points += 2
            "我趁他不注意，看到了他國中時期的照片，表情比現在柔和許多。"
            b1 "...不准看。"
        "聽話地繼續整理文件。":
            $ lujingze_points += 1
            "結束時，學長遞給我一罐冰涼的果汁。"
            b1 "辛苦了。做得不錯。"
    jump day_3_lunch

label day_2_event_luoxinghuai:
    scene bg computer_lab with fade
    "我來到電腦教室，裡面只有洛星淮一個人。"
    show b2_uniform at pos_right
    b2 "啊，語夏...妳來了。"
    show g1_uniform at pos_left
    g1 "這就是你做的遊戲嗎？好厲害！"
    b2 "還只是個雛形...對了，妳之前答應要幫忙的NPC，我已經建好模型了，妳要看看嗎？"
    menu:
        "「好啊！我很期待！」":
            $ luoxinghuai_points += 2
            b2 "我希望...她能成為這個世界裡，最溫暖的存在..."
        "「在你旁邊看你製作就好。」":
            $ luoxinghuai_points += 1
    jump day_3_lunch
    
# --- 週三・午休 & 放學後 | 全員集合的日常 ---
label day_3_lunch:
    scene bg classroom with fade
    "週三的午休，我們四個人難得地聚在教室裡一起吃午餐。"
    "雖然互動不多，但能這樣聚在一起，就讓人覺得很平靜。"
    jump day_3_afterschool

label day_3_afterschool:
    "放學後，我們又順路一起回家。"
    g1 "（平淡的日常，卻也讓人感到安心。）"
    jump day_4_lunch

# --- 週四・午休 & 放學後 | 籃球場的風雲 ---
label day_4_lunch:
    scene bg classroom with fade
    "週四午休，林曉興沖沖地跑來告訴我。"
    show g2_uniform at pos_right
    g2 "語夏！今天下午有校隊的公開練習賽耶！去看陸景澤學長比賽吧！"
    show g1_uniform at pos_left
    g1 "好啊！"
    jump day_4_afterschool

label day_4_afterschool:
    scene bg basketball_court with fade
    "下午，我們來到球場邊的板凳席觀戰。"
    show b1_basketball at pos_center
    "陸景澤學長在場上表現非常出色，但中途似乎扭到了一下腳，被教練換下場休息。"
    hide b1_basketball
    show b1_basketball at pos_farright
    show g1_uniform at pos_leftcenter
    show g2_uniform at pos_farleft
    show b2_uniform at pos_rightcenter
    g1 "（學長好像受傷了...看起來很懊惱的樣子。）"
    menu:
        "立刻跑過去，遞上運動噴霧。":
            $ lujingze_points += 2
            $ linxiao_points -= 1
            g1 "學長，你還好嗎？這個給你！"
            b1 "...我沒事。"
        "拜託洛星淮去看看情況。":
            $ luoxinghuai_points += 1
            $ lujingze_points += 1
            g1 "洛同學，你和學長比較熟，可以幫我去看看情況嗎？"
            b2 "嗯，好。"
        "和林曉一起為場上的其他隊員加油。":
            $ linxiao_points += 1
            $ lujingze_points -= 2
            g1 "（學長自尊心很強，現在過去可能會打擾他...）"
    jump day_5_lunch

# --- 週五・午休 & 放學後 | 比賽前的約定 ---
label day_5_lunch:
    scene bg classroom with fade
    "週五午休，大家聚在一起，氣氛卻有些不同。"
    show g1_uniform at pos_rightcenter
    show g2_uniform at pos_leftcenter
    show b1_uniform at pos_farleft
    show b2_uniform at pos_farright
    
    b2 "明天...就是秋季賽的第一場了。"
    "洛星淮的聲音很平靜，卻帶著一絲不易察覺的緊張。"
    g2 "哇！那必須去加油啊！我們大家一起去給淮神助威吧！"
    b1 "......"
    "陸景澤學長沒有說話，但也沒有反對。"
    jump day_5_afterschool

label day_5_afterschool:
    "放學後，我們一起走到校門口。"
    hide g2_uniform
    hide b1_uniform
    show b2_uniform at pos_right
    b2 "那...明天早上十點，在市中心的電競館，如果大家方便的話..."
    show g1_uniform at pos_left
    g1 "我一定會去的！"
    "我看著他，想給他一些鼓勵。"
    menu:
        "「明天的比賽，我會一直看著你的。」":
            $ luoxinghuai_points += 1
            "洛星淮的輪廓似乎愣了一下，然後輕輕地點了點頭。"
        "「大家一起去幫你加油，你一定沒問題的！」":
            $ linxiao_points += 1
            "林曉開心地附和：「對啊對啊！」"
        "「學長和曉曉也會一起去的吧？」":
            $ lujingze_points += 1
            "我把話題拋給了另外兩人，陸景澤學長只是「嗯」了一聲。"

    "就這樣，我們定下了週末的計畫，為明天的比賽做好了約定。"
    jump day_6_esports_competition

# --- 週六・週末 | 榮耀之日 (大型電競比賽) ---
label day_6_esports_competition:
    scene bg esports_arena with fade
    "週六，我準時來到了市中心的電競比賽會場。"
    "巨大的舞台、閃爍的燈光、震耳欲聾的音樂和觀眾的歡呼聲，這一切都讓我感到既新奇又震撼。"
    
    show g1_casual at pos_t_center
    show g2_casual at pos_t_right
    show b1_casual at pos_t_left
    
    g2 "哇塞！這也太帥了吧！比我們想像的還要誇張耶！"
    b1 "吵死了。"
    
    "比賽開始了，洛星淮和ZACY戰隊的隊員們登上了舞台。"
    hide g1_casual
    hide g2_casual
    hide b1_casual
    show b2_esports at pos_center
    "聚光燈下的他，穿著黑白相間的ZACY戰隊隊服，戴著專業的隔音耳機，表情專注而冷酷，和平時溫柔的樣子判若兩人。"
    
    "比賽進行得異常激烈，到了決勝的第三局，ZACY戰隊陷入了前所未有的劣勢。"
    hide b2_esports
    show g1_casual at pos_t_center
    show g2_casual at pos_t_right
    show b1_casual at pos_t_left
    
    g2 "怎麼會這樣...加油啊！"
    b1 "對方的策略很有針對性，封鎖了打野的遊走空間。"
    g1 "（洛星淮...）"
    "我看著大螢幕上他緊抿的嘴唇，心也跟著揪了起來。"
    "在這一刻，我應該..."

    menu:
        "（眼神與他交會，露出充滿信任和鼓勵的微笑。）":
            $ luoxinghuai_points += 3
            $ lujingze_points -= 1
            "下一刻，被稱為『淮神』的他，上演了一場驚天逆轉的完美操作！"
        "（和林曉一起，大聲為ZACY戰隊加油吶喊。）":
            $ linxiao_points += 2
            $ luoxinghuai_points += 1
            "我們熱烈的加油聲，似乎也感染了周圍的粉絲，整個會場的氣氛達到了頂點。"
        "（緊張地握緊雙手，向身旁的陸景澤尋求分析。）":
            $ lujingze_points += 2
            $ luoxinghuai_points -= 1
            g1 "學長...你覺得，還有機會贏嗎？"
            b1 "有。但要看他敢不敢賭。"
    
    "最終，在全場的歡呼聲中，ZACY戰隊贏得了比賽！"
    hide g1_casual
    hide g2_casual
    hide b1_casual
    show b2_casual at pos_center
    "洛星淮在接受採訪後，換回了便服，第一時間來到了我們面前，他的臉上帶著疲憊，但更多的是喜悅。"
    jump day_7_afternoon

# --- 週日・黃昏 | 吊橋上的決心 (最終抉擇) ---
label day_7_afternoon:
    scene bg suspension_bridge with fade
    "週日的黃昏，結束了愉快又疲憊的週末。"
    "我們又走到了那座橫跨在河上的吊橋。"
    show g1_casual at pos_rightcenter
    show g2_casual at pos_leftcenter
    show b1_casual at pos_farleft
    show b2_casual at pos_farright
    g1 "（我...好像必須要做出選擇了。）"
    menu:
        "（我想要走向...那個總是默默守護，卻又無比可靠的身影。）":
            jump confession_lujingze
        "（我想要走向...那個永遠像太陽一樣，帶給我溫暖和快樂的身影。）":
            jump confession_linxiao
        "（我想要走向...那個能理解我內心，帶我進入全新世界的身影。）":
            jump confession_luoxinghuai
        "（我...還無法決定...）":
            jump normal_ending_leadup

################################################################################
# Part 5: 結局分支 (Ending Branches)
################################################################################

label normal_ending_leadup:
    "我站在原地，沒有走向任何人。"
    "這個夏天...還很長，或許，維持現狀就是最好的答案。"
    "我們的故事，未完待續。"
    return

# --- 各角色告白與後續劇情 ---
label confession_lujingze:
    scene bg basketball_court
    show g1_uniform at pos_left
    show b1_basketball at pos_right
    "幾天後，我被陸景澤學長單獨約到了放學後的籃球場。"
    b1 "林語夏，我喜歡妳。"
    menu:
        "我...我也喜歡學長。":
            jump lujingze_good_end_path
        "對不起...可以給我一點時間嗎？":
            jump common_hesitate_path

label confession_linxiao:
    scene bg suspension_bridge
    show g1_casual at pos_left
    show g2_casual at pos_right
    "就在那個黃昏的吊橋上，林曉拉住了我的手。"
    g2 "林語夏，我喜歡妳！是戀愛的那種喜歡！"
    menu:
        "曉曉...其實我也...":
            jump linxiao_good_end_path
        "我...我一直把妳當成最好的朋友...":
            jump common_hesitate_path

label confession_luoxinghuai:
    scene bg airplane
    show g1_casual at pos_left
    show b2_casual at pos_right
    "......後來，我答應了和洛星淮一起，代表學校去國外參加一個遊戲創作比賽。"
    "在飛往國外的飛機上..."
    b2 "語夏。我喜歡妳，可以讓妳...成為我世界裡，永遠的女主角嗎？"
    menu:
        "我願意。":
            jump luoxinghuai_good_end_path
        "我...腦子有點亂，對不起...":
            jump common_hesitate_path

# --- 告白後續分支 ---
label lujingze_good_end_path:
    g1 "我...我也是...一直都...喜歡著學長。"
    b1 "...笨蛋，這種事...不早點說。"
    return

label linxiao_good_end_path:
    g1 "曉曉...其實我...好像也是一樣的..."
    g2 "太好了...太好了語夏！我還以為會被妳討厭..."
    return

label luoxinghuai_good_end_path:
    g1 "我願意...成為你世界的女主角。"
    b2 "謝謝妳，語夏。"
    return

label common_hesitate_path:
    g1 "對不起...我...我需要一點時間想一想..."
    return

################################################################################
# --- 《夏日海灘篇》完整故事線 ---
################################################################################
label beach_chapter:
    scene bg beach_day with fade
    
    # --- 開場（到達海邊） ---
    "炙熱的陽光、鹹鹹的海風、以及海浪拍打沙灘的聲音，宣告著夏天的正式到來。"
    show g2_casual at pos_left
    show g1_casual at pos_right
    g2 "哇～海風好舒服啊！語夏，快看那邊的浪花～"
    g1 "真的耶，好久沒來海邊了。"
    
    hide g1_casual
    hide g2_casual
    
    show b2_casual at pos_left
    show b1_casual at pos_right
    b2 "（戴著墨鏡，拿著飲料）……人好多。"
    b1 "（提著行李）別跑太快，小心摔倒。"
    
    "我們在沙灘上找到了休息的地方，燦爛的夏日物語，就此展開。"
    jump beach_event_1

# --- 事件 1：泳裝小插曲 ---
label beach_event_1:
    "安頓好後，林曉立刻拉著我衝向海邊的出租店。"
    show g2_casual at pos_right
    show g1_casual at pos_left
    hide b1_casual
    hide b2_casual
    
    g2 "換泳裝換泳裝！來海邊就是要穿得可愛一點啊！"
    g2 "語夏～這件粉色比基尼超適合你！"
    g1 "欸！？太、太害羞了啦！"
    
    "正當我們吵吵鬧鬧時，兩個身影也走了過來。"
    hide g1_casual
    hide g2_casual
    show g1_casual at pos_leftcenter
    show g2_casual at pos_rightcenter
    show b1_casual at pos_farleft
    show b2_casual at pos_farright
    
    b1 "……選妳喜歡的，不要勉強。"
    b2 "（小聲）嗯…但她穿起來一定很好看。"
    g1 "（真是的...他們怎麼都過來了啦...）"
    
    menu:
        "「那、那我就試試看這件...」 (鼓起勇氣)":
            $ beach_linxiao_points += 1
            $ beach_luoxinghuai_points += 1
            $ beach_lujingze_points += 1
            g1 "既然曉曉都這麼說了...那我就試試看好了..."
        "「我還是選那件連身的好了...」 (保守選擇)":
            g1 "我還是比較習慣連身的款式，這件粉色的就很好看。"
        "「你們兩個男生為什麼要跟過來啊！」 (害羞地抱怨)":
            $ beach_lujingze_points += 2
            g1 "真是的！為什麼你們要跟過來啦！"
            b1 "...吵死了。誰想跟著妳。"
            b2 "抱歉...我們只是路過..."

    jump beach_event_2

# --- 事件 2：沙灘排球 ---
label beach_event_2:
    "午後，我們決定來一場沙灘排球比賽。"
    hide g1_casual
    hide g2_casual
    hide b1_casual
    hide b2_casual
    
    show g1_swimsuit at pos_leftcenter
    show g2_swimsuit at pos_farleft
    show b1_swimsuit at pos_farright
    show b2_swimsuit at pos_rightcenter

    "我和林曉一隊，陸景澤和洛星淮一隊。"
    b2 "（冷酷接球）得分。"
    g2 "星淮你好厲害！"
    "輪到我發球時，我緊張地將球拋起，卻不小心打偏了方向。"
    g1 "啊！"
    
    menu:
        "（感覺到一陣強風，陸景澤擋在了我面前）":
            $ beach_lujingze_points += 2
            b1 "妳沒事吧？小心點…"
        "（感覺到有人從旁邊拉了我一把，是洛星淮）":
            $ beach_luoxinghuai_points += 2
            b2 "還好嗎？有沒有嚇到？"
        "（林曉從背後抱住了我，一起摔在沙灘上）":
            $ beach_linxiao_points += 2
            g2 "好險好險！嚇死我了！語夏妳沒受傷吧？"

    jump beach_event_3

# --- 事件 3：夕陽下的心事 ---
label beach_event_3:
    scene bg beach_sunset with fade
    "傍晚，夕陽將整片海染成了溫暖的橘紅色。"
    "這是一個適合談心的時刻，而我..."

    menu:
        "走向獨自看著海的陸景澤。":
            jump beach_talk_lujingze
        "走向安靜地堆著沙堡的洛星淮。":
            jump beach_talk_luoxinghuai
        "走向正在追逐浪花的林曉。":
            jump beach_talk_linxiao

# --- 個人談心劇情 ---
label beach_talk_lujingze:
    $ beach_lujingze_points += 2
    hide g2_swimsuit
    hide b2_swimsuit
    show g1_swimsuit at pos_left
    show b1_swimsuit at pos_right
    g1 "學長，你在想什麼呢？"
    b1 "海風很吵，但我還是聽得見妳的聲音。"
    jump beach_event_4

label beach_talk_luoxinghuai:
    $ beach_luoxinghuai_points += 2
    hide g2_swimsuit
    hide b1_swimsuit
    show g1_swimsuit at pos_left
    show b2_swimsuit at pos_right
    g1 "好厲害...你怎麼堆得這麼好？"
    b2 "妳看夕陽時發呆的樣子…讓我很想保護妳。"
    jump beach_event_4

label beach_talk_linxiao:
    $ beach_linxiao_points += 2
    hide b1_swimsuit
    hide b2_swimsuit
    show g1_swimsuit at pos_left
    show g2_swimsuit at pos_right
    "我們並肩坐在沙灘上。"
    g2 "語夏…我…想要妳永遠把我放在身邊。"
    jump beach_event_4

# --- 高潮（夜晚煙火） ---
label beach_event_4:
    scene bg beach_night with fade
    "夜幕降臨，沙灘上點燃了燦爛的煙火。"
    show g1_casual at pos_rightcenter
    show g2_casual at pos_leftcenter
    show b1_casual at pos_farleft
    show b2_casual at pos_farright
    
    g2 "好漂亮啊！語夏，快看～"
    g1 "（這個夏天，像煙火一樣閃耀，卻也短暫...）"
    "煙火的光芒映照著每個人的側臉，也照亮了我心中的答案。"
    
    if beach_lujingze_points > beach_linxiao_points and beach_lujingze_points > beach_luoxinghuai_points:
        jump beach_lujingze_end
    elif beach_linxiao_points > beach_lujingze_points and beach_linxiao_points > beach_luoxinghuai_points:
        jump beach_linxiao_end
    elif beach_luoxinghuai_points > beach_lujingze_points and beach_luoxinghuai_points > beach_linxiao_points:
        jump beach_luoxinghuai_end
    else:
        jump beach_friendship_end

# --- 夏日篇結局 ---
label beach_lujingze_end:
    "煙火的光芒下，陸景澤突然輕聲對我說——"
    b1 "我喜歡妳。"
    g1 "（臉紅）我…我也是。"
    return

label beach_luoxinghuai_end:
    "洛星淮遞上一邊耳機，讓我聽他最喜歡的音樂。"
    b2 "下次比賽…妳能繼續為我加油嗎？"
    g1 "嗯！一定會的！"
    return

label beach_linxiao_end:
    "林曉緊緊地握住了我的手，眼神比煙火還要明亮。"
    g2 "語夏，我不想只是妳的朋友。"
    g1 "（心跳加快，卻也微笑）我知道了。"
    return

label beach_friendship_end:
    "我們四個人一起點燃了仙女棒，在沙灘上追逐嬉戲。"
    g1 "（這就是我們的夏天，沒有誰缺席。）"
    return
    "故事，未完待續。"
    return
