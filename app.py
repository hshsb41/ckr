from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

<title>CKRPRO TOOLS</title>

<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/lucide@latest"></script>

<style>
* {
    -webkit-tap-highlight-color: transparent;
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #080a0f;
    color: #fff;
    font-family: Inter, Arial, sans-serif;
    overflow-x: hidden;
}

/* INTRO SPLASH OVERLAY */
#intro-overlay {
    position: fixed;
    inset: 0;
    background: #080a0f;
    z-index: 99999;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    transition: opacity 0.5s ease, visibility 0.5s ease;
}

/* Sano ra Golo Logo */
.clean-logo {
    width: 65px;
    height: 65px;
    border-radius: 50%;
    object-fit: cover;
    cursor: pointer;
    transition: transform 0.2s ease;
}

.clean-logo:active {
    transform: scale(0.9);
}

.tool-card {
    background: #10131a;
    transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-decoration: none;
    color: inherit;
}

.tool-card:active {
    transform: scale(0.98);
}

/* Colorful Icon Boxes - No Glow */
.icon-box {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Color Classes */
.bg-blue-soft { background: rgba(59, 130, 246, 0.1); color: #3b82f6; }
.bg-green-soft { background: rgba(34, 197, 94, 0.1); color: #22c55e; }
.bg-purple-soft { background: rgba(168, 85, 247, 0.1); color: #a855f7; }
.bg-orange-soft { background: rgba(249, 115, 22, 0.1); color: #f97316; }
.bg-red-soft { background: rgba(239, 68, 68, 0.1); color: #ef4444; }

.search-box {
    background: #10131a;
}

.wa-btn {
    background: #20c875;
    transition: transform 0.2s ease;
}

.fade {
    animation: fade .25s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fade {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
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
    <img src="https://i.ibb.co/Y4KjTgvP/Picsart-26-02-07-02-21-57-621.jpg" alt="Logo" id="logo-btn" class="clean-logo mb-4">
    <p class="text-[9px] text-gray-600 font-bold tracking-widest uppercase"></p>
</div>

<!-- DASHBOARD CONTENT -->
<section id="tools" class="max-w-6xl mx-auto px-4 pt-6">

    <div class="flex items-center justify-between mb-3">
        <div>
            <h2 class="font-black text-lg"> </h2>
            <p class="text-[11px] text-gray-600 mt-0.5">
                
            </p>
        </div>

        <span id="count" class="text-[10px] font-bold text-gray-500 bg-[#11151d] px-2 py-1 rounded">
            7 TOOLS
        </span>
    </div>

    <div class="search-box rounded-xl px-3 py-3 flex items-center gap-3 mb-3">
        <i data-lucide="search" class="w-4 h-4 text-gray-500"></i>
        <input id="search" type="text" placeholder="Search tools..." 
               class="w-full bg-transparent outline-none text-sm placeholder:text-gray-600">
    </div>


    <!-- FILTERS -->
    <div class="flex gap-2 overflow-x-auto pb-4">
        <button class="filter active px-3 py-2 rounded-lg bg-white text-black text-[10px] font-black" data-filter="all">ALL</button>
        <button class="filter px-3 py-2 rounded-lg bg-[#11151d] text-gray-400 text-[10px] font-black" data-filter="token">TOKEN</button>
        <button class="filter px-3 py-2 rounded-lg bg-[#11151d] text-gray-400 text-[10px] font-black" data-filter="freefire">FREE FIRE</button>
        <button class="filter px-3 py-2 rounded-lg bg-[#11151d] text-gray-400 text-[10px] font-black" data-filter="premium">PREMIUM</button>
    </div>


    <!-- TOOL GRID -->
    <div id="toolGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 pb-12">

        <!-- TOOL 1 -->
        <a href="https://eat-to-access-token-by-ckrpro-web-g.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool" data-category="token freefire" data-name="eat to access token">
            <div>
                <div class="flex items-start justify-between">
                    <div class="icon-box bg-blue-soft">
                        <i data-lucide="key-round" class="w-5 h-5"></i>
                    </div>
                    <span class="text-[9px] font-black text-emerald-400">● ONLINE</span>
                </div>
                <h3 class="mt-4 text-sm font-black uppercase">EAT TO ACCESS TOKEN</h3>
                <p class="text-[11px] text-gray-500 mt-1.5 leading-5"> </p>
            </div>
            <div class="mt-5 flex items-center justify-between text-[10px] font-bold text-gray-500">
                <span>TAP TO OPEN</span>
                <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </div>
        </a>

        <!-- TOOL 2 -->
        <a href="https://free-fire-glory-bot-ckr-and-bbc-web.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool" data-category="freefire premium" data-name="buy glory bot paid">
            <div>
                <div class="flex items-start justify-between">
                    <div class="icon-box bg-purple-soft">
                        <i data-lucide="crown" class="w-5 h-5"></i>
                    </div>
                    <span class="text-[9px] font-black text-emerald-400">● ONLINE</span>
                </div>
                <h3 class="mt-4 text-sm font-black uppercase">BUY GLORY BOT PAID</h3>
                <p class="text-[11px] text-gray-500 mt-1.5 leading-5"> </p>
            </div>
            <div class="mt-5 flex items-center justify-between text-[10px] font-bold text-gray-500">
                <span>TAP TO OPEN</span>
                <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </div>
        </a>

        <!-- TOOL 3 -->
        <a href="https://ff-ckrpro-request-spam-and-profile.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool" data-category="freefire" data-name="request spam profile visit">
            <div>
                <div class="flex items-start justify-between">
                    <div class="icon-box bg-green-soft">
                        <i data-lucide="send" class="w-5 h-5"></i>
                    </div>
                    <span class="text-[9px] font-black text-emerald-400">● ONLINE</span>
                </div>
                <h3 class="mt-4 text-sm font-black uppercase">REQUEST SPAM & VISIT</h3>
                <p class="text-[11px] text-gray-500 mt-1.5 leading-5"> </p>
            </div>
            <div class="mt-5 flex items-center justify-between text-[10px] font-bold text-gray-500">
                <span>TAP TO OPEN</span>
                <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </div>
        </a>

        <!-- TOOL 4 -->
        <a href="https://ckrpro-bio-changer-with-access-toke.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool" data-category="freefire token" data-name="long bio changer">
            <div>
                <div class="flex items-start justify-between">
                    <div class="icon-box bg-orange-soft">
                        <i data-lucide="file-pen-line" class="w-5 h-5"></i>
                    </div>
                    <span class="text-[9px] font-black text-emerald-400">● ONLINE</span>
                </div>
                <h3 class="mt-4 text-sm font-black uppercase">LONG BIO CHANGER</h3>
                <p class="text-[11px] text-gray-500 mt-1.5 leading-5"> </p>
            </div>
            <div class="mt-5 flex items-center justify-between text-[10px] font-bold text-gray-500">
                <span>TAP TO OPEN</span>
                <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </div>
        </a>

        <!-- TOOL 5 -->
        <a href="https://ff-get-eat-token-webtool.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool" data-category="token freefire" data-name="get eat token">
            <div>
                <div class="flex items-start justify-between">
                    <div class="icon-box bg-blue-soft">
                        <i data-lucide="ticket" class="w-5 h-5"></i>
                    </div>
                    <span class="text-[9px] font-black text-emerald-400">● ONLINE</span>
                </div>
                <h3 class="mt-4 text-sm font-black uppercase">GET EAT TOKEN</h3>
                <p class="text-[11px] text-gray-500 mt-1.5 leading-5"> </p>
            </div>
            <div class="mt-5 flex items-center justify-between text-[10px] font-bold text-gray-500">
                <span>TAP TO OPEN</span>
                <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </div>
        </a>

        <!-- TOOL 6 -->
        <a href="https://guild-join-and-leave-webtool-ckr.vercel.app/" target="_blank"
           class="tool-card rounded-2xl p-4 tool" data-category="freefire" data-name="guild manager">
            <div>
                <div class="flex items-start justify-between">
                    <div class="icon-box bg-green-soft">
                        <i data-lucide="users-round" class="w-5 h-5"></i>
                    </div>
                    <span class="text-[9px] font-black text-emerald-400">● ONLINE</span>
                </div>
                <h3 class="mt-4 text-sm font-black uppercase">GUILD MANAGER</h3>
                <p class="text-[11px] text-gray-500 mt-1.5 leading-5"> </p>
            </div>
            <div class="mt-5 flex items-center justify-between text-[10px] font-bold text-gray-500">
                <span>TAP TO OPEN</span>
                <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </div>
        </a>

        <!-- TOOL 7 -->
        <a href="https://ckrprolike.up.railway.app/#auto-likes" target="_blank"
           class="tool-card rounded-2xl p-4 tool" data-category="freefire premium" data-name="ckrpro paid like">
            <div>
                <div class="flex items-start justify-between">
                    <div class="icon-box bg-red-soft">
                        <i data-lucide="heart" class="w-5 h-5"></i>
                    </div>
                    <span class="text-[9px] font-black text-emerald-400">● ONLINE</span>
                </div>
                <h3 class="mt-4 text-sm font-black uppercase">CKRPRO PAID LIKE</h3>
                <p class="text-[11px] text-gray-500 mt-1.5 leading-5"> </p>
            </div>
            <div class="mt-5 flex items-center justify-between text-[10px] font-bold text-gray-500">
                <span>TAP TO OPEN</span>
                <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </div>
        </a>

    </div>
</section>

<!-- FOOTER -->
<footer class="pb-10 opacity-30 text-center">
    <div class="text-[9px] font-black tracking-[4px] uppercase"> </div>
</footer>

<!-- FLOATING WHATSAPP -->
<a href="https://wa.me/9779840825493" target="_blank"
   class="fixed right-4 bottom-4 z-50 w-12 h-12 rounded-full wa-btn flex items-center justify-center shadow-xl">
    <i data-lucide="message-circle" class="w-5 h-5 text-black"></i>
</a>

<script>
lucide.createIcons();

const search = document.getElementById("search");
const cards = [...document.querySelectorAll(".tool")];
const count = document.getElementById("count");
const filters = document.querySelectorAll(".filter");
const logoBtn = document.getElementById("logo-btn");
const introOverlay = document.getElementById("intro-overlay");
const bgMusic = document.getElementById("bg-music");

logoBtn.addEventListener("click", () => {
    bgMusic.play().catch(e => console.log("Music error"));
    introOverlay.style.opacity = "0";
    setTimeout(() => {
        introOverlay.style.display = "none";
    }, 500);
});

function updateTools() {
    const query = search.value.toLowerCase().trim();
    const currentFilter = document.querySelector(".filter.active").dataset.filter;
    let visible = 0;

    cards.forEach(card => {
        const name = card.dataset.name.toLowerCase();
        const category = card.dataset.category.toLowerCase();
        const matchesSearch = name.includes(query);
        const matchesFilter = currentFilter === "all" || category.includes(currentFilter);

        if (matchesSearch && matchesFilter) {
            card.style.display = "flex";
            visible++;
        } else {
            card.style.display = "none";
        }
    });
    count.textContent = visible + " TOOLS";
}

search.addEventListener("input", updateTools);

filters.forEach(button => {
    button.addEventListener("click", () => {
        filters.forEach(x => {
            x.classList.remove("active", "bg-white", "text-black");
            x.classList.add("bg-[#11151d]", "text-gray-400");
        });
        button.classList.add("active", "bg-white", "text-black");
        button.classList.remove("bg-[#11151d]", "text-gray-400");
        updateTools();
    });
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
