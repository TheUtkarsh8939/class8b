<script>
  let lander;
  const size = "10"

  let columns = Math.round(document.body.clientWidth / size);
  let rows = Math.round(window.innerHeight/ size);
    console.log(columns,rows,size,window.innerHeight)
</script>

<div class="lander" id="lander" bind:this={lander}>
    {#each Array(rows).fill(0) as _, index}
    <div class="row">
        {#each Array(columns).fill(0) as _, index}
        <div class="square"></div>
      {/each}
    </div>
  {/each}
</div>

<style>

  .lander {
    height: calc(100vh + 100px);
    width: 100vw;
    background: radial-gradient(
      ellipse at center,
      var(--primary-color),
      var(--background),
      var(--lighter-bg)
    );
    overflow:hidden;
    gap:2px;
    display: flex;
    flex-direction: column;
    position: absolute;
    z-index:-1
  }
  .row{
    display: flex;
    background-color: transparent;
    gap:2px;
  }
  .square{
    
    height:100px;
    aspect-ratio: 1/1;
    background-color: var(--lighter-bg);
  }
</style>
