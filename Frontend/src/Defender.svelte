<script>
  import axios from 'axios';
  import { push, pop, replace } from 'svelte-spa-router';
  import { onMount } from 'svelte';

  let headlines = '';
  let image = '';
  let description = '';
  
  let categories = [];

  const fetch = async () => {
    const id = document.querySelector('select').value;
    var res = await axios({
      method: 'post',
      url: 'http://localhost:3003/news/',
      data: {
        categoriesId: id,
        headlines: headlines,
        image: image,
        description: description,
        categories: categories,
      },
    });
    console.log(res.data);
    push('/');
  };

  onMount(async () => {
    var res = await axios({
      method: 'get',
      url: 'http://localhost:3003/categories',
    });
    categories = res.data;
  });
</script>

<div>
  <p class="head">OSINT for Network Defenders</p>
  <p>
    The benefits of using Open Source Network Intelligence for those defending
    an organisation is not as obvious as for those working on the offensive
    side.
  </p>
  <p>
    Understanding the network footprinting and reconnaissance methodology can
    help to inform your security posture, discover assets that you may not have
    even been aware of and allow for prioritised mitigation against the most
    likely systems to be attacked.
  </p>
  <p class="head">Network Reconnaissance for Asset Discovery</p>
  <p>
    Performing an open source intelligence based assessment of your
    organisations network can inform a number of different security related
    objectives.
  </p>
  <p>
    Of course any mature security practice should have up to date and accurate
    asset records, that provide all of this information. The important thing to
    note is that often these asset registers are not accurate or even exist and
    by performing assessments from the attackers perspective you can focus on
    the same areas as the attackers.
  </p>
  <p class="head">Identify Gaps in Security Architecture</p>
  <p>
    By having a map of your attack surface from the attackers perspective you
    are able to identify gaps in your security architecture. Be they Security
    Logging, Network Monitoring Systems (IDS / IPS) or Firewalls. Identify the
    gaps and mitigate.
  </p>
  <p>
    Now for a hasty security analogy; It is no good having a big lock on the
    front door if the side window has been left open.
  </p>
  <p>
    Use Network Based OSINT to Map Attackers Infrastructure Defenders can gather
    network focused open source intelligence on IP addresses that are attacking
    (or have successfully compromised) their organisation. The intelligence
    could include operating systems, web applications, DNS related data and even
    patch levels from banners. All gathered passively. This can be combined with
    threat intelligence feeds to develop a profile on the attacker.
  </p>
  <p>
    As a simple example perhaps you are responding to a number of security
    incidents. When analysing the TTP's (tactics, techniques & procedures) of
    the attackers you notice that while the separate incidents have been sourced
    to separate network blocks there are characteristics in network OSINT of the
    attacking servers that may actually link the attacks.
  </p>
  <p>
    With a major advantage being the fact that by using these techniques your
    reconnaissance is passive in nature. Ensuring that the attacker will not be
    aware of your investigation.
  </p>
  <p class="head">Assess Network Perimeter without the Paper Work</p>
  <p>
    Defenders using open source network intelligence have the advantage of
    assessing networks without having to go through any lengthy change approval
    process. Many organisations have strict approvals required for any active
    scanning of perimeter systems, so the clear advantage is that your OSINT
    based reconnaissance has no impact.
  </p>
  <p>
    It is of course highly recommended that you have approval to assess the
    network in question from your management to ensure there are no awkward
    meetings where you have to explain why you were assessing the network when
    you are the company accountant.
  </p>
  <p>
    For organisations whose security practice is less mature, you may be able to
    develop a detailed open source intelligence based report on your
    organisation with minimal approval. Using the report to push for further
    more active testing either by your internal teams, external service
    providers or maybe even get a bug bounty program off the ground.
  </p>
  <p class="foot">More to Come - Sign up to the mailing list for updates.</p>
</div>

<style>
  div {
    padding-top: 10px;
    padding-left: 0px;
    padding-right: 75%;
    align-items: center;
  }
  .foot {
    color: rgb(5, 56, 5);
  }
  .head{
    font-display: bold;
  }
</style>
