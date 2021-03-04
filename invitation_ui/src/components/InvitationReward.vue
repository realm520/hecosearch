<template>
<v-container>
<v-card>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title>{{this.$route.query.address}}</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title><b>Totally</b> <v-btn text color="primary">{{ total | showValue }}</v-btn> Reward from Invitee: </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
</v-card>
  <v-simple-table dense>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">Block</th>
          <th class="text-left">Invitee</th>
          <th class="text-left">Reward</th>
          <!-- <th class="text-left">Level</th> -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in rewards" :key="item.blockNum">
          <td>{{ item.blockNum }}</td>
          <td>{{ item.sub | showAddress }}</td>
          <td>{{ item.reward | showValue }}</td>
          <!-- <td>{{ item.subLevel }}</td> -->
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</v-container>
</template>

<script>
export default {
  name: "InvitationReward",

  data: () => ({
    rewards: [
    ],
    total: 0
  }),
  created() {
      let _this = this
      console.log((this.$route.query.coin))
      console.log((this.$route.query.address))
      if (typeof(this.$route.query.address) != "undefined" && typeof(this.$route.query.coin) != "undefined") {
          console.log('in')
          this.$api.get_invitation_reward(this.$route.query.address, this.$route.query.coin).then(response => {
              _this.rewards = response
              _this.total = 0
              let i
              for (i in response) {
                  console.log(i)
                _this.total += Number(response[i].reward)
              }
          })
      }
  },
  filters: {
    showAddress(address) {
      if (address.length <= 14) {
        return address;
      }
      const a = address.slice(0, 6);
      const b = address.slice(address.length - 4, address.length);
      return a + "···" + b;
    },
    showValue(value) {
        return Number(value).toFixed(2)
    }
  }
};
</script>
