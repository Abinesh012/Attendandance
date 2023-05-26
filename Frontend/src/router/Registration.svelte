<script>
  import { push } from 'svelte-spa-router';
  import axios from 'axios';

  let roll_number = '';
  let email = '';
  let phone_number = '';
  let first_name = '';
  let last_name = '';
  let password = '';
  let department = '';
  let selectedOption = 'Select an option';
  let isOpen = false;

  function goto() {
    push('#/login');
  }

  function handleRegistration() {
    // Perform registration logic here
    console.log('Email:', email);
    console.log('Phone number', phone);
    console.log('First Name', first_name);
    console.log('Last Name', last_name);
    console.log('Password:', password);
    console.log('Department', department);
    console.log('rollno', roll_number);
    console.log('usertyper', selectedOption);
  }

  const fetch = async () => {
    const res = await axios({
      method: 'post',
      url: 'http://192.168.1.240:5000/api/signup',
      data: {
        roll_number: roll_number,
        first_name: first_name,
        last_name: last_name,
        department: department,
        user_type: selectedOption,
        email: email,
        phone_number: phone_number,
        password: password,
      },
    });
    push('/login');
  };

  function toggleDropdown() {
    isOpen = !isOpen;
  }

  function selectOption(option) {
    selectedOption = option;
    isOpen = false;
  }
</script>

<main>
  <form on:submit|preventDefault={fetch}>
    <div>
      <label for="rollno">Roll Number:</label>
      <input type="text" id="rollnumber" bind:value={roll_number} required />

      <label for="firstname">First Name:</label>
      <input type="text" id="firstname" bind:value={first_name} required />

      <label for="lastname">Last Name:</label>
      <input type="text" id="lastname" bind:value={last_name} required />

      <label for="department">Department:</label>
      <input type="text" id="department" bind:value={department} required />

      <div class="dropdown" on:click={toggleDropdown}>
        <div class="dropdown__button">
          {selectedOption}
        </div>

        {#if isOpen}
          <ul class="dropdown__list">
            <li class="dropdown__item" on:click={() => selectOption('Staff')}>
              Staff
            </li>
            <li class="dropdown__item" on:click={() => selectOption('Student')}>
              Student
            </li>
            <li class="dropdown__item" on:click={() => selectOption('Hod')}>
              Hod
            </li>
          </ul>
        {/if}
      </div>

      <label for="email">Email:</label>
      <input type="text" id="emailid" bind:value={email} required />

      <label for="phonenumber">Phone Number:</label>
      <input type="text" id="phone" bind:value={phone_number} required />

      <label for="password">Password:</label>
      <input type="password" id="password" bind:value={password} required />

      <button type="submit">Register</button>
    </div>
  </form>
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    font-family: Arial, sans-serif;
  }

  form {
    display: flex;
    flex-direction: column;
    width: 300px;
  }

  label {
    margin-bottom: 0.5rem;
    font-weight: bold;
  }

  input {
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  button {
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }

  .dropdown {
    position: relative;
    display: inline-block;
  }

  .dropdown__list {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    padding: 0.5rem;
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    /* display:  isopen? "block" : 'none'; */
  }

  .dropdown__item {
    padding: 0.25rem 0.5rem;
    cursor: pointer;
  }

  .dropdown__item:hover {
    background-color: #f0f0f0;
  }
</style>
