<script>
  import axios from 'axios';
  import { push } from 'svelte-spa-router';

  let roll_number = '';
  let password = '';

  function goto() {
    push('/home');
  }

  const fetch = async () => {
    const res = await axios({
      method: 'post',
      url: 'http://192.168.1.240:5000/api/login/status',
      data: {
        roll_number: roll_number,
        password: password,
      },
    });
    console.log(res.data);
    if (res.data.user_type == 'student') {
      push('/home');
    } else if (res.data.user_type == 'staff') {
      push('/staff');
    } else {
      push('/hod');
    }
  };
</script>

<div class="container">
  <h2>Login</h2>

  <form on:submit|preventDefault={fetch}>
    <div class="form-group">
      <label for="username">Username:</label>
      <input type="text" id="username" bind:value={roll_number} required />
    </div>

    <div class="form-group">
      <label for="password">Password:</label>
      <input type="password" id="password" bind:value={password} required />
    </div>

    <button type="submit" class="submit-btn">Login</button>
  </form>
</div>

<style>
  .container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }

  .form-group {
    margin-bottom: 20px;
  }

  .form-group label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
  }

  .form-group input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }

  .submit-btn {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #05740a;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  .submit-btn:hover {
    background-color: #4caf50;
  }
</style>
