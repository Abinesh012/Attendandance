<script>
  let attendees = [
    { id: 1, name: 'John Doe', department:'MSc',status: 'Present' },
    { id: 2, name: 'Jane Smith',department:'MSc',status: 'Absent' },
    { id: 3, name: 'Robert Johnson',department:'MSc', status: 'Present' },
    { id: 4, name: 'Emily Davis', department:'MSc',status: 'Present' },
    { id: 5, name: 'Michael Wilson',department:'MSc', status: 'Absent' },
  ];

  function updateStatus(id, newStatus) {
    attendees = attendees.map((attendee) => {
      if (attendee.id === id) {
        return { ...attendee, status: newStatus };
      }
      return attendee;
    });
  }
</script>

<main>
  <h1>Student Attendance</h1>

  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Department</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      {#each attendees as attendee}
        <tr>
          <td>{attendee.id}</td>
          <td>{attendee.name}</td>
          <td>{attendee.department}</td>
          <td>{attendee.status}</td>
          <td>
            <button on:click={() => updateStatus(attendee.id, 'Present')}
              >View</button
            >
          </td>
        </tr>
      {/each}
    </tbody>
  </table>
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

  h1 {
    margin-bottom: 1rem;
  }

  table {
    border-collapse: collapse;
    width: 400px;
  }

  th,
  td {
    padding: 0.5rem;
    text-align: left;
    border-bottom: 1px solid #ccc;
  }

  th {
    background-color: #f0f0f0;
  }

  td button {
    padding: 0.25rem 0.5rem;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  td button:hover {
    background-color: #0056b3;
  }
</style>
