<script lang="ts">
	import Header from '$lib/header/Header.svelte';
	import '../app.css';
</script>

<Header />

<main>
	<slot />
</main>

<footer>
	Members
	<ul>
		<li>Angel Paul Agnabo</li>
		<li>Cherilyn Radam</li>
		<li>Don Gumayagay</li>
		<li>Francis Chez</li>
		<li>Krisna John Belay</li>
		<li>Ryan Bernardo Abellar</li>
		<li>Sine Nale</li>
		<li>Victoria Louise</li>
	</ul>
</footer>

<style>
	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 1024px;
		margin: 0 auto;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 40px;
	}

	@media (min-width: 480px) {
		footer {
			padding: 40px 0;
		}
	}
</style>
