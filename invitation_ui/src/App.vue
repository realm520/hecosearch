<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <v-spacer></v-spacer>

    </v-app-bar>

    <v-main>
        <v-container>
      <router-view></router-view>
        </v-container>
    </v-main>
  </v-app>
</template>

<script>
// import InvitationReward from './components/InvitationReward';

export default {
  name: 'App',

//   components: {
//     InvitationReward,
//   },

  data: () => ({
    //
  }),
};
</script>
