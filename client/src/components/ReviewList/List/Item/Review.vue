<script>
    export default {
        props: {
            item: {
                type: Array,
                default: [],
            }
        },

        computed: {
            formatItems() {
                let result = ''

                if (this.item) {
                    this.item.forEach((value) => {
                    result += `\n - ${value}`
                    })
                }   
                

                return result
            }
        },

        mounted() {
            console.log(this.item)
        }
    }
</script>

<template>
    <div class="review">
        {{ formatItems }}
    </div>
</template>

<style lang="scss" scoped>
    .review {
        color: var(--secondary-text);
        font-family: var(--main-font);
        font-weight: 200;
        white-space: pre;
    }
</style>