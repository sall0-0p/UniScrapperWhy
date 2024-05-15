<script>
    import ProductList from '../components/ProductList/ProductList.vue'
    import PageHeader from '../components/Header/Header.vue'
    
    export default {
        components: {
            ProductList,
            PageHeader,
        },

        props: {
            selected: {
                type: String,
                default: '',
            },
        }
    }
</script>

<template>
    <div class='main'>
        <PageHeader
            :selected="selected"
        />
        <ProductList>
            
        </ProductList>
    </div>
</template>

<style lang="scss" scoped>
    .main {
        display: flex;
        flex-direction: column;
    }
</style>