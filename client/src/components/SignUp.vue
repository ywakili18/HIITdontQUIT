<template>
    <div>
        <h2>Welcome to HIITDONTQUIT</h2>
        <p>We're very excited to have you join and start creating and tracking your workouts!</p>
        <p>Please fill out the information below to get started</p>
        <br/>
        <br/>
        <br/>
        <section>
            <form>
                <h6>What is your first and last name?</h6>
                
                <input type='text' placeholder="First Name"/>
                <br/>
                <br/>
                <input type='text' placeholder="Last Name"/>
                <br/>
                <br/>
                <h6>Now, additional information</h6>
                <input type='number' placeholder="Weight"/>
                <br/>
                <input type='number' placeholder="Height in inches"/>
                <br/>
                <input type='number' placeholder="Age"/>
                <br/>
                <br/>
                <h6>Now Set a goal for yourself!</h6>
                <input type="number" placeholder="Goal Weight" />
                <br/>
                <br/>
                <h6>And now to make it official</h6>
                <br/>
                <input type="email" placeholder=" Enter Email"/>
                <br/>
                <br/>
                <input type="text" placeholder="Create Username" />
                <br/>
                <br/>
                <input type="password" placeholder="Create Password" />
                <br/>
                <br/>
                <input type="password" placeholder="Confirm Password" />
                <br/>
                <br/>
                <button>Create Account</button>

            </form>
        </section>
    </div>
   
</template>


<script>
export default {
    name: 'SignUp'
}
</script>



<style scoped>

</style>
