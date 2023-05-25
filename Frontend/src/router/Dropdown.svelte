<script>
  export let options = [];
  export let selectedOption = null;

  let isOpen = false;

  function toggleDropdown() {
    isOpen = !isOpen;
  }

  function selectOption(option) {
    selectedOption = option;
    isOpen = false;
  }
</script>

<div class="dropdown">
  <button class="dropdown__button" on:click={toggleDropdown}>
    {#if selectedOption}
      {selectedOption}
    {:else}
      Select an option
    {/if}
  </button>

  {#if isOpen}
    <ul class="dropdown__list">
      {#each options as option}
        <li class="dropdown__item" on:click={() => selectOption(option)}>
          {option}
        </li>
      {/each}
    </ul>
  {/if}
</div>

<style>
  .dropdown {
    position: relative;
    display: inline-block;
  }

  .dropdown__button {
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  .dropdown__list {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    padding: 0;
    margin: 0;
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }

  .dropdown__item {
    padding: 0.5rem 1rem;
    cursor: pointer;
  }

  .dropdown__item:hover {
    background-color: #f0f0f0;
  }
</style>
