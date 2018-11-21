<template>

    <v-timeline align-top>
        <v-timeline-item
                v-for="(item, i) in items"
                :color="item.color"
                :icon="item.icon"
                :key="i"
                fill-dot
        >
            <v-card
                    :color="item.color"
                    dark
            >
                <v-card-title class="title">{{ item.text }}</v-card-title>
                <v-card-text v-if="item.buttons.length > 0" class="white text--primary">
                    <!--<p>{{ item.body }}</p>-->
                    <v-btn v-for="but in item.buttons"
                           :color="item.color"
                           class="mx-0"
                           outline
                           @click="postUserInput(item, but.text)"
                    >
                        {{ but.text }}
                    </v-btn>
                </v-card-text>
            </v-card>
        </v-timeline-item>
    </v-timeline>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Conversation",
        data: () => ({
            items: []
        }),
        methods: {
            loadInitialNode() {
                return axios.get('/api/conversations/' + this.$route.params.convId + '/');
            },
            postUserInput(item, text) {
                axios.post('/api/userinputs/', {text: text, conversation: this.$route.params.convId}).then(resp => {
                    item.buttons = [];
                    this.items.push({
                        text: resp.data.text,
                        body: '',
                        color: 'green lighten-1',
                        icon: 'mdi-airballoon',
                        buttons: []
                    });
                    setTimeout(() => {  // Lets humanize it a bit :) hehe
                        this.items.push({
                            text: resp.data.current_node.text,
                            body: '',
                            color: 'purple darken-1',
                            icon: 'mdi-book-variant',
                            buttons: resp.data.current_node.answer_variants
                        })
                    }, 800);

                });
            },
        },
        mounted() {
            this.loadInitialNode().then(resp => {
                this.items.push({
                    text: resp.data.questionnarie.root_node.text,
                    body: '',
                    color: 'purple darken-1',
                    icon: 'mdi-book-variant',
                    buttons: resp.data.questionnarie.root_node.answer_variants
                })
            })
        },
    }
</script>

<style scoped>

</style>