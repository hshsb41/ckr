from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

<title> </title>

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
    width: 70px;
    height: 70px;
    border-radius: 50%;
    object-fit: cover;
    cursor: pointer;
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

.clean-logo:hover {
    transform: scale(1.05);
}

.clean-logo:active {
    transform: scale(0.92);
}

/* TOOL CARDS (Album Grid Style) */
.tool-card {
    background: #0e1117;
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-decoration: none;
    color: inherit;
    border: none;
    aspect-ratio: 1 / 0.95;
}

.tool-card:hover {
    background: #131720;
    transform: translateY(-2px);
}

.tool-card:active {
    transform: scale(0.96);
}

/* Soft Icon Boxes */
.icon-box {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Premium Soft Colors */
.bg-blue-soft { background: rgba(59, 130, 246, 0.08); color: #3b82f6; }
.bg-green-soft { background: rgba(34, 197, 94, 0.08); color: #22c55e; }
.bg-purple-soft { background: rgba(168, 85, 247, 0.08); color: #a855f7; }
.bg-orange-soft { background: rgba(249, 115, 22, 0.08); color: #f97316; }
.bg-red-soft { background: rgba(239, 68, 68, 0.08); color: #ef4444; }
.bg-yellow-soft { background: rgba(234, 179, 8, 0.08); color: #eab308; }

.search-box {
    background: #0e1117;
    transition: background 0.2s ease;
}

.search-box:focus-within {
    background: #131720;
}

.wa-btn {
    background: #10b981;
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.wa-btn:active {
    transform: scale(0.9);
}

::-webkit-scrollbar { width: 0; }
</style>
</head>

<body>

<!-- AUDIO PLAYER -->
<audio id="bg-music" preload="auto" loop>
    <source src="{{ url_for('static', filename='music.mp3') }}" type="audio/mpeg">
</audio>

<!-- INTRO SPLASH SCREEN -->
<div id="intro-overlay">
    <img src="https://i.ibb.co/Y4KjTgvP/Picsart-26-02-07-02-21-57-621.jpg" alt="Logo" id="logo-btn" class="clean-logo mb-3">
    <span class="text-[10px] text-gray-500 font-semibold tracking-widest uppercase animate-pulse"></span>
</div>

<!-- DASHBOARD CONTENT -->
<section id="tools" class="max-w-5xl mx-auto px-4 pt-8">

    <div class="flex items-center justify-between mb-4">
        <div>
            <h1 class="font-extrabold text-xl tracking-tight text-white"></h1>
            <p class="text-[11px] text-gray-400 mt-0.5 font-medium">
                
            </p>
        </div>

        <span id="count" class="text-[10px] font-bold text-gray-400 bg-[#0e1117] px-2.5 py-1.5 rounded-xl border border-white/5">
            
        </span>
    </div>

    <!-- SEARCH BOX -->
    <div class="search-box rounded-xl px-3.5 py-2.5 flex items-center gap-3 mb-6 border border-white/5">
        <i data-lucide="search" class="w-4 h-4 text-gray-500"></i>
        <input id="search" type="text" placeholder=" " 
               class="w-full bg-transparent outline-none text-xs text-white placeholder:text-gray-500">
    </div>

    <!-- ALBUM GRID (Unified Single Grid) -->
    <div id="toolGrid" class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3.5 pb-16">

        <!-- TOOL 1 -->
        <a href="https://eat-to-access-token-by-ckrpro-web-g.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool border border-white/5" data-name="eat to access token">
            <div>
                <div class="icon-box bg-blue-soft">
                    <i data-lucide="key-round" class="w-5 h-5"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[11px] font-medium text-gray-500 tracking-wide">
                <span>EAT TOKEN</span>
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 text-gray-600"></i>
            </div>
        </a>

        <!-- TOOL 2 -->
        <a href="https://free-fire-glory-bot-ckr-and-bbc-web.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool border border-white/5" data-name="glory bot">
            <div>
                <div class="icon-box bg-purple-soft">
                    <i data-lucide="crown" class="w-5 h-5"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[11px] font-medium text-gray-500 tracking-wide">
                <span>GLORY BOT</span>
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 text-gray-600"></i>
            </div>
        </a>

        <!-- TOOL 3 -->
        <a href="https://ff-ckrpro-request-spam-and-profile.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool border border-white/5" data-name="request spam profile visit">
            <div>
                <div class="icon-box bg-green-soft">
                    <i data-lucide="send" class="w-5 h-5"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[11px] font-medium text-gray-500 tracking-wide">
                <span>SPAM & VISIT</span>
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 text-gray-600"></i>
            </div>
        </a>

        <!-- TOOL 4 -->
        <a href="https://ckrpro-bio-changer-with-access-toke.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool border border-white/5" data-name="long bio">
            <div>
                <div class="icon-box bg-orange-soft">
                    <i data-lucide="file-pen-line" class="w-5 h-5"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[11px] font-medium text-gray-500 tracking-wide">
                <span>LONG BIO</span>
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 text-gray-600"></i>
            </div>
        </a>

        <!-- TOOL 5 -->
        <a href="https://ff-get-eat-token-webtool.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool border border-white/5" data-name="get eat token">
            <div>
                <div class="icon-box bg-blue-soft">
                    <i data-lucide="ticket" class="w-5 h-5"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[11px] font-medium text-gray-500 tracking-wide">
                <span>GET TOKEN</span>
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 text-gray-600"></i>
            </div>
        </a>

        <!-- TOOL 6 -->
        <a href="https://guild-join-and-leave-webtool-ckr.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool border border-white/5" data-name="guild manager">
            <div>
                <div class="icon-box bg-green-soft">
                    <i data-lucide="users-round" class="w-5 h-5"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[11px] font-medium text-gray-500 tracking-wide">
                <span>GUILD MANAGER</span>
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 text-gray-600"></i>
            </div>
        </a>

        <!-- TOOL 7 -->
        <a href="https://ckrlike.up.railway.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool border border-white/5" data-name="like bot">
            <div>
                <div class="icon-box bg-red-soft">
                    <i data-lucide="heart" class="w-5 h-5"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[11px] font-medium text-gray-500 tracking-wide">
                <span>LIKE BOT</span>
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 text-gray-600"></i>
            </div>
        </a>

        <!--  -->
        <a href="https://freefire-private-topup-ckrpro.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool border border-white/5" data-name="ff topup">
            <div>
                <div class="icon-box bg-yellow-soft">
                    <i data-lucide="zap" class="w-5 h-5"></i>
                </div>
            </div>
            <div class="flex items-center justify-between text-[11px] font-medium text-gray-500 tracking-wide">
                <span>FF TOPUP</span>
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 text-gray-600"></i>
            </div>
        </a>

    </div>
</section>

<!-- FLOATING WHATSAPP -->
<a href="https://wa.me/9779840825493" target="_blank"
   class="fixed right-5 bottom-5 z-50 w-12 h-12 rounded-full wa-btn flex items-center justify-center shadow-xl">
    <i data-lucide="message-circle" class="w-5 h-5 text-black"></i>
</a>

<script>
lucide.createIcons();

const search = document.getElementById("search");
const cards = [...document.querySelectorAll(".tool")];
const count = document.getElementById("count");
const logoBtn = document.getElementById("logo-btn");
const introOverlay = document.getElementById("intro-overlay");
const bgMusic = document.getElementById("bg-music");

logoBtn.addEventListener("click", () => {
    bgMusic.play().catch(e => console.log("Audio play blocked"));
    introOverlay.style.opacity = "0";
    setTimeout(() => {
        introOverlay.style.display = "none";
    }, 400);
});

function updateTools() {
    const query = search.value.toLowerCase().trim();
    let visible = 0;

    cards.forEach(card => {
        const name = card.dataset.name.toLowerCase();
        const matchesSearch = name.includes(query);

        if (matchesSearch) {
            card.style.display = "flex";
            visible++;
        } else {
            card.style.display = "none";
        }
    });
    count.textContent = visible + " TOOLS";
}

search.addEventListener("input", updateTools);
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
