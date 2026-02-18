<div class="form-card">
	<h2>Log In</h2>
	<form onsubmit={(e) => e.preventDefault()}>
		<label>
			Email
			<input type="email" placeholder="reader@gmail.com" required />
		</label>
		<label>
			Password
			<input type="password" placeholder="********" required />
		</label>
		<button type="submit">Enter the Library</button>
	</form>
</div>

<style>
	.form-card {
		width: 100%;
		max-width: 400px;
		padding: 2.5rem;
		border: 1px solid var(--border);
		border-radius: 4px;
	}

	h2 {
		color: var(--gold);
		font-size: 1.8rem;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		text-align: center;
		margin-bottom: 2rem;
	}

	form {
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
	}

	label {
		display: flex;
		flex-direction: column;
		gap: 0.4rem;
		font-size: 0.9rem;
		color: var(--text-muted);
	}

	input {
		padding: 0.7rem 0.9rem;
		background: transparent;
		border: 1px solid var(--border);
		border-radius: 3px;
		color: var(--text);
		font-family: var(--font);
		font-size: 1rem;
	}

	input:focus {
		outline: none;
		border-color: var(--gold);
	}

	button {
		margin-top: 0.5rem;
		padding: 0.75rem;
		background: var(--gold);
		color: var(--bg);
		border: none;
		border-radius: 3px;
		font-family: var(--font);
		font-size: 1rem;
		letter-spacing: 0.05em;
		cursor: pointer;
	}

	button:hover {
		opacity: 0.9;
	}
</style>
