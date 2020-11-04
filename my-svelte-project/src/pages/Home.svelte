<script>
    import {onMount} from 'svelte';
    import PostForm from '../components/PostForm.svelte';

    const apiBaseUrl = 'https://ndb99xkpdk.execute-api.eu-west-2.amazonaws.com/dev';

    let posts = [];
    onMount(async () => {

        const res = await fetch(apiBaseUrl + '/posts');
        posts = await res.json();
    }
    
    )


    function editPost(post){
        console.log(post);
    }
    function deletePost(id){
        console.log('Deleting post with id: ', id);
    }
</script>


<style>
    .delete-btn{
        color: red !important;
    }

    .card .card-content .card-content{
        margin-bottom: 0;
    }
    .card .card-content p.timestamp {
        margin-bottom: 0;
    }
</style>


<div class="row">
<div class="col s6">
    <PostForm></PostForm>
</div>

</div>
<div class="row">
{#if posts.length === 0}
<h3>Loading posts ....</h3>
{:else}
{#each posts as post}
<div class="col s6">
    <div class="card">
        <div class="card-content">
            <p class="card-title">{posts.title}</p>
            <p class="timestamp">{posts.createdAt}</p>
            <p>{posts.body}</p>
        </div>
        <div class="card-action">
            <a href="#" on:click={() => editPost(post)}> Edit</a>
            <a href="#" class="delete-btn" on:click= { ()=> deletePost(posts.id)}> Delete</a>
        </div>
    </div>
</div>
    
{/each}
{/if}




</div>
