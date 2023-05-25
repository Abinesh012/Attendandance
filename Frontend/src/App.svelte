<script>
  import Router from 'svelte-spa-router';
  import Home from './router/Home.svelte';
  import Login from './router/Login.svelte';
  import Registration from './router/Registration.svelte';
  import Staff from './router/Staff.svelte';
  import Hod from './router/Hod.svelte';

  let routes = {
    '/home': Home,
    '/login': Login,
    '/register': Registration,
    '/staff': Staff,
    '/hod': Hod,
  };
</script>

<main>
  <nav>
    <ul class="nav-menu">
      <li><a href="#/home" class="nav-item">Home</a></li>
      <li><a href="#/login" class="nav-item">Login</a></li>
      <li><a href="#/register" class="nav-item">Register</a></li>
      <li><a href="#/staff" class="nav-item">Staff</a></li>
      <li><a href="#/hod" class="nav-item">HOD</a></li>
    </ul>
  </nav>
  <Router {routes} />
</main>

<style>
  nav {
    background-color: #007bff;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .nav-menu {
    list-style: none;
    display: flex;
    gap: 1rem;
  }
  .nav-item {
    color: #fff;
    text-decoration: none;
  }
  .nav-item:hover {
    text-decoration: underline;
  }
</style>
