from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

<title>MY STORE</title>

<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/lucide@latest"></script>

<style>
* {
    -webkit-tap-highlight-color: transparent;
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #06080d;
    color: #f3f4f6;
    font-family: Inter, system-ui, -apple-system, sans-serif;
    overflow-x: hidden;
}

/* INTRO SPLASH OVERLAY */
#intro-overlay {
    position: fixed;
    inset: 0;
    background: #06080d;
    z-index: 99999;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    transition: opacity 0.4s ease, visibility 0.4s ease;
}

.clean-logo {
    width: 65px;
    height: 65px;
    border-radius: 50%;
    object-fit: cover;
    cursor: pointer;
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    border: 2px solid rgba(255, 255, 255, 0.08);
}

.clean-logo:hover {
    transform: scale(1.05);
}

.clean-logo:active {
    transform: scale(0.92);
}

/* COMPACT TOOL CARDS */
.tool-card {
    background: #0e1117;
    transition: transform 0.2s ease, background-color 0.2s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-decoration: none;
    color: inherit;
    border: 1px solid rgba(255, 255, 255, 0.05);
    aspect-ratio: 1 / 0.85;
}

.tool-card:hover {
    background: #131720;
    transform: translateY(-2px);
    border-color: rgba(255, 255, 255, 0.12);
}

.tool-card:active {
    transform: scale(0.96);
}

/* Icon Boxes */
.icon-box {
    width: 34px;
    height: 34px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Soft Colors */
.bg-blue-soft { background: rgba(59, 130, 246, 0.1); color: #3b82f6; }
.bg-green-soft { background: rgba(34, 197, 94, 0.1); color: #22c55e; }
.bg-purple-soft { background: rgba(168, 85, 247, 0.1); color: #a855f7; }
.bg-orange-soft { background: rgba(249, 115, 22, 0.1); color: #f97316; }
.bg-red-soft { background: rgba(239, 68, 68, 0.1); color: #ef4444; }
.bg-yellow-soft { background: rgba(234, 179, 8, 0.1); color: #eab308; }
.bg-pink-soft { background: rgba(236, 72, 153, 0.1); color: #ec4899; }

.wa-btn {
    background: #10b981;
    transition: transform 0.25s ease;
    box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
}

.wa-btn:active {
    transform: scale(0.9);
}

::-webkit-scrollbar { width: 0; }
</style>
</head>

<body>

<!-- AUDIO PLAYER WITH DIRECT RELILABLE LINK -->
<audio id="bg-music" preload="auto" loop>
    <source src="https://www.bensound.com/bensound-music/bensound-dubstep.mp3" type="audio/mpeg">
</audio>

<!-- INTRO SPLASH SCREEN -->
<div id="intro-overlay">
    <img src="https://i.ibb.co/Y4KjTgvP/Picsart-26-02-07-02-21-57-621.jpg" alt="Logo" id="logo-btn" class="clean-logo mb-2">
    <span class="text-[9px] text-gray-500 font-bold tracking-widest uppercase animate-pulse">Tap to Enter</span>
</div>

<!-- DASHBOARD CONTENT -->
<section class="max-w-4xl mx-auto px-3 pt-6 pb-14">

    <div class="mb-5 text-center">
        <h1 class="text-xl font-black tracking-tight text-white">MY STORE</h1>
    </div>

    <!-- ALBUM GRID -->
    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2.5">

        <!-- MY STORE LINK -->
        <a href="https://ckrstore.up.railway.app" target="_blank"
           class="tool-card rounded-xl p-3">
            <div>
                <div class="icon-box bg-pink-soft">
                    <i data-lucide="store" class="w-4 h-4"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[10px] font-bold text-gray-300 mt-2">
                <span>MY STORE</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3 text-gray-400"></i>
            </div>
        </a>

        <!-- TOOL 1 -->
        <a href="https://eat-to-access-token-by-ckrpro-web-g.vercel.app/" target="_blank"
           class="tool-card rounded-xl p-3">
            <div>
                <div class="icon-box bg-blue-soft">
                    <i data-lucide="key-round" class="w-4 h-4"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[10px] font-medium text-gray-400 mt-2">
                <span>EAT TOKEN</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3 text-gray-500"></i>
            </div>
        </a>

        <!-- TOOL 2 -->
        <a href="https://free-fire-glory-bot-ckr-and-bbc-web.vercel.app/" target="_blank"
           class="tool-card rounded-xl p-3">
            <div>
                <div class="icon-box bg-purple-soft">
                    <i data-lucide="crown" class="w-4 h-4"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[10px] font-medium text-gray-400 mt-2">
                <span>GLORY BOT</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3 text-gray-500"></i>
            </div>
        </a>

        <!-- TOOL 3 -->
        <a href="https://ff-ckrpro-request-spam-and-profile.vercel.app/" target="_blank"
           class="tool-card rounded-xl p-3">
            <div>
                <div class="icon-box bg-green-soft">
                    <i data-lucide="send" class="w-4 h-4"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[10px] font-medium text-gray-400 mt-2">
                <span>SPAM & VISIT</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3 text-gray-500"></i>
            </div>
        </a>

        <!-- TOOL 4 -->
        <a href="https://ckrpro-bio-changer-with-access-toke.vercel.app/" target="_blank"
           class="tool-card rounded-xl p-3">
            <div>
                <div class="icon-box bg-orange-soft">
                    <i data-lucide="file-pen-line" class="w-4 h-4"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[10px] font-medium text-gray-400 mt-2">
                <span>LONG BIO</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3 text-gray-500"></i>
            </div>
        </a>

        <!-- TOOL 5 -->
        <a href="https://ff-get-eat-token-webtool.vercel.app/" target="_blank"
           class="tool-card rounded-xl p-3">
            <div>
                <div class="icon-box bg-blue-soft">
                    <i data-lucide="ticket" class="w-4 h-4"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[10px] font-medium text-gray-400 mt-2">
                <span>GET TOKEN</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3 text-gray-500"></i>
            </div>
        </a>

        <!-- TOOL 6 -->
        <a href="https://guild-join-and-leave-webtool-ckr.vercel.app/" target="_blank"
           class="tool-card rounded-xl p-3">
            <div>
                <div class="icon-box bg-green-soft">
                    <i data-lucide="users-round" class="w-4 h-4"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[10px] font-medium text-gray-400 mt-2">
                <span>GUILD MGR</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3 text-gray-500"></i>
            </div>
        </a>

        <!-- TOOL 7 -->
        <a href="https://ckrlike.up.railway.app/" target="_blank"
           class="tool-card rounded-xl p-3">
            <div>
                <div class="icon-box bg-red-soft">
                    <i data-lucide="heart" class="w-4 h-4"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[10px] font-medium text-gray-400 mt-2">
                <span>LIKE BOT</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3 text-gray-500"></i>
            </div>
        </a>

        <!-- TOOL 8 -->
        <a href="https://freefire-private-topup-ckrpro.vercel.app/" target="_blank"
           class="tool-card rounded-xl p-3">
            <div>
                <div class="icon-box bg-yellow-soft">
                    <i data-lucide="zap" class="w-4 h-4"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[10px] font-medium text-gray-400 mt-2">
                <span>FF TOPUP</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3 text-gray-500"></i>
            </div>
        </a>

    </div>
</section>

<!-- FLOATING WHATSAPP -->
<a href="https://wa.me/9779840825493" target="_blank"
   class="fixed right-4 bottom-4 z-50 w-10 h-10 rounded-full wa-btn flex items-center justify-center">
    <i data-lucide="message-circle" class="w-5 h-5 text-black"></i>
</a>

<script>
lucide.createIcons();

const logoBtn = document.getElementById("logo-btn");
const introOverlay = document.getElementById("intro-overlay");
const bgMusic = document.getElementById("bg-music");

logoBtn.addEventListener("click", () => {
    bgMusic.play().then(() => {
        console.log("Audio playing successfully");
    }).catch(e => {
        console.log("Audio play blocked:", e);
    });
    
    introOverlay.style.opacity = "0";
    setTimeout(() => {
        introOverlay.style.display = "none";
    }, 400);
});
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

