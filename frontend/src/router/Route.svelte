<script>
  import {Router, Route} from "svelte-routing";
  import Home from "../components/Home.svelte";
  import About from "../components/About.svelte";
  export let url = "";
</script>
<Router {url}>
  <Route path="/" component={Home} />
  <Route path="about" component={About} />
</Router>
