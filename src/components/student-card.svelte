<script>
  import { onMount } from "svelte";

    export let name = ""
    export let tag = ""
    export let image = "./default.jpg"
    export let fontSize = "1rem"
  

</script>
<div class="relative flex justify-center items-center w-[170px]">
    <div class="card-border">
        <div class="card relative">
            <img src={image} alt="" class="absolute">
            <div class="h-full w-full ovr absolute"></div>
            <span class="text-shadow font-alex text-xl text-white absolute bottom-0 left-1 tagger"><strong>{name}</strong><br> <span style="font-size:{fontSize}">{tag}</span></span>
        </div>
    </div>
    <div class="shadow absolute bottom-[-10px]"></div>
</div>
<style>
    *{
        cursor:default;
        caret-color: transparent;
    }
    .card-border{
        background: conic-gradient(from -45deg, #0000, #0000 150deg, var(--darker-primary) 180deg, var(--primary-color) 270deg, #0000 300deg);
        height: 174px;
        width: 172px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 20px;
        position: relative;
        z-index: 1;
    }
    .shadow{
        position: absolute;
        background:linear-gradient(90deg, var(--secondry-color), var(--primary-color));
        filter: blur(20px);
        height: 17px;
        width: 150px;
    }
    .card{
        background-color: var(--background);
        height: 170px;
        width:170px;
        border-radius: 20px;
    }   
    img{
        width:170px;
        border-radius: 20px 20px 20px 20px;
    }
    .text-shadow{
        text-shadow:0px 0px 13px black;

    }
    .ovr{
        border-radius: 20px 20px 20px 20px;
        background: linear-gradient(180deg, transparent, rgba(0, 0, 0, 0.537));
        transition: 500ms all;
    }
    .ovr:hover{
        opacity: 0;
    }
    .ovr:hover ~ .tagger{
        transition: 0.7s all ease;
        opacity: 0;
    }

    .font-alex{
        font-family: "Alex Brush";
    }
</style>
