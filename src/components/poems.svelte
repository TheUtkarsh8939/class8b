<script>

  export let author = ""
  const arrayOfPoems = [
  {
    id:"st1",
    author: "Srishti",
    name: "Aaj bhi",
    body: `Aaj bhi yaad aati hai vo din ki, jab pehli bar<br/>
          Tujhe uss chote se taron Jaisi jhund mein....
          `,
  },
  {
    id:"ut1",
    author: "Utkarsh",
    name: "When I saw her",
    body : `When I saw her,<br/>
for the first time in my life<br/>
I started daydreaming about her......`
  },
    {
    id:"ut2",
    author: "Utkarsh",
    name: "क्या है मन मैं तेरे?",
    body : `हाट में है बाजार लगे<br/>
गलियों में सजे नज़ारे......`
  },
      {
     id:"ut3",
    author: "Utkarsh",
    name: "Doing, Doing, Doing",
    body : `Doing, Doing, Doing,<br/> 
things on repeat`
  },
];
</script>
{#each arrayOfPoems as poem}
{#if author === ""}
<a href={"/poems/"+poem.id}>
  <div
  class="peom flex flex-col w-screen pl-10 pt-4 pb-8 border-t-2 border-t-[var(--lighter-primary)]"
>
  <span class="text-2xl font-bold">{poem.name}</span>
  <span>By {poem.author}</span>
  <span class="text-xs ml-4 mt-2">
    { @html poem.body}
  </span>
</div>
</a>
{:else}
{#if author===poem.author}
<a href={"/poems/"+poem.id}>
  <div
  class="peom flex flex-col w-screen pl-10 pt-4 pb-8 border-t-2 border-t-[var(--lighter-primary)]"
>
  <span class="text-2xl font-bold">{poem.name}</span>
  <span>By {poem.author}</span>
  <span class="text-xs ml-4 mt-2">
    { @html poem.body}
  </span>
</div>
</a>
{/if}
{/if}
{/each}
