<script>
    export default {
        props: {
            item: {
                type: Array,
                default: [],
            },
            prefix: {
                type: String,
                default: '-',
            },
        },

        computed: {
            formatItems() {
                let result = ''

                if (this.item) {
                    this.item.forEach((value) => {
                    result += `\n ${this.prefix} ${value}`
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