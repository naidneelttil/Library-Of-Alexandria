<script>
	import '../app.css';

	let { children } = $props();
</script>

<nav>
	<a href="/" class="brand">Library of Alexandria</a>
	<div class="nav-right">
		<a href="/login">Log in</a>
		<a href="/signup">Sign up</a>
	</div>
</nav>

<main>
	{@render children()}
</main>

<style>
	nav {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 1rem 2rem;
		border-bottom: 1px solid var(--border);
	}

	.brand {
		font-size: 1.2rem;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--gold);
	}

	.nav-right {
		display: flex;
		gap: 1.5rem;
	}

	main {
		display: flex;
		justify-content: center;
		align-items: center;
		min-height: calc(100vh - 60px);
	}
</style>
