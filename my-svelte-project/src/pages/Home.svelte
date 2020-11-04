<script>
    import {onMount} from 'svelte';
    const apiBaseUrl = 'https://ndb99xkpdk.execute-api.eu-west-2.amazonaws.com/dev';

    let posts = [];
    onMount(async () => {

        const res = await fetch(apiBaseUrl + '/posts');
        posts = await res.json();
    }
    
    )
</script>

<div class="row">
{#if posts.length === 0}
<h3>Loading posts ....</h3>
{:else}
{#each posts as post}
<div class="col s6">
    <div class="card">
        <div class="card-content">
            <p class="card-title">{posts.title}</p>
            <p>{posts.createdAt}</p>
            <p>{posts.body}</p>
        </div>
    </div>
</div>
    
{/each}
{/if}




</div>
