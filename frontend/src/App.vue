<template>
    <v-app id="inspire">
        <v-navigation-drawer
                v-model="drawer"
                fixed
                app
        >
            <v-list dense>
                <v-list-tile to="/">
                    <v-list-tile-action>
                        <v-icon>home</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>Questionnaires List</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>
        <v-toolbar color="purple darken-1" dark fixed app>
            <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
            <v-toolbar-title>Questionnaires App</v-toolbar-title>
        </v-toolbar>
        <v-content>
            <v-container fluid >
                <router-view></router-view>
            </v-container>
        </v-content>
        <!--<v-footer color="green lighten-1" app>-->
            <!--<span class="white&#45;&#45;text">&copy; 2018</span>-->
        <!--</v-footer>-->
    </v-app>
</template>

<script>
    export default {
        data: () => ({
            drawer: false
        }),
        props: {
            source: String
        }
    }
</script>