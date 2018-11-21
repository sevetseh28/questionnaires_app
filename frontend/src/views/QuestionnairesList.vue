<template>
    <v-layout row>
        <v-flex xs12 sm6 offset-sm3>
            <v-card>
                <v-toolbar color="green lighten-1" dark>

                    <v-toolbar-title class="text-xs-center">Questionnaires List</v-toolbar-title>

                    <v-spacer></v-spacer>

                </v-toolbar>

                <v-list subheader>
                    <v-list-tile
                            v-for="item in items"
                            :key="item.id"
                            avatar
                            @click="createConversation(item.id)"
                    >
                        <v-list-tile-content>
                            <v-list-tile-title v-html="item.description"></v-list-tile-title>
                        </v-list-tile-content>

                        <v-list-tile-action>
                            <v-icon :color="item.active ? 'teal' : 'grey'">chat_bubble</v-icon>
                        </v-list-tile-action>
                    </v-list-tile>
                </v-list>


            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "QuestionnairesList",
        data() {
            return {
                items: []
            }
        },
        methods: {
            getDataFromApi() {
                return axios.get('/api/questionnaires/');
            },

            createConversation(id_quest) {
                return axios.post('/api/conversations/', {"questionnarie": id_quest}).then(resp => {
                    let convId = resp.data.id;
                    this.$router.push({ name: 'conversation', params: { convId: convId }}) // Start conversation
                });
            }
        },
        mounted() {
            this.getDataFromApi()
                .then(resp => {
                    this.items = resp.data;
                })
        },
    }
</script>

<style scoped>

</style>