<script>
    import PageHeader from '../components/Header/Header.vue'

    export default {
        components: {
            PageHeader,
        },

        data() {
            return {
                productId: this.$route.params.productId,
                item: {},
            }
            },

            methods: {
            async fetchAll() {
                const responce = await this.repository.getProductData(this.productId);
                const rawJSON = await responce.json();
                this.item = await JSON.parse(rawJSON);
            }
        },
    }
</script>

<template>
    <div class='main'>
        <PageHeader
            selected="Product Charts"
        />  
    </div>
</template>

<style>

</style>