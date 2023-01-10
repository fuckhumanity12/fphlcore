<script>
    import { link, links } from "svelte-routing";
</script>
<nav class="navbar mx-auto navbar-expand-lg bg-light" use:links>
    <div class="container-fluid">
        <a class="navbar-brand" href="/">FPHL 🕵🏻‍♀️🕵🏻‍♂️</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/">Home</a>
                </li>
                <li class="nav-item dropdown active">
                    <button class="nav-link active border border-0 bg-light dropdown-toggle" data-bs-toggle="dropdown"
                        aria-expanded="false">
                        Subjects
                </button>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="/subject/General">General</a></li>
                        <li><a class="dropdown-item" href="/subject/Phonetics">Phonetics</a></li>
                        <li><a class="dropdown-item" href="/subject/Linguistics">Linguistics</a></li>
                        <li><a class="dropdown-item" href="/subject/Phonology">Phonology</a></li>
                        <li><a class="dropdown-item" href="/subject/English">English</a></li>
                        <li><a class="dropdown-item" href="/subject/Communication Skills">Communication Skills</a></li>
                        <li><a class="dropdown-item" href="/subject/Law">Law</a></li>
                    </ul>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" href="/about">About Us</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" href="/contact">Contact Us</a>
                </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="/account"><i class="fa-solid fa-user"></i> Account</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="/auth/logout"><i class="fa-solid fa-door-open"></i> Logout</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-primary active" href="/auth/login"><i class="fa-solid fa-user"></i> Login</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-success active" href="/auth/register"><i class="fa-sharp fa-solid fa-right-href-bracket"></i> Register</a>
                    </li>
            </ul>
            <form class="d-flex" method="GET" action="" role="search">
                
                <input class="form-control me-2" name="q" type="text" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
        </div>
    </div> 
</nav>