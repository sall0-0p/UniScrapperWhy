<script>
    export default {
        props: {
            review: {
                type: Object,
                default: () => ({}),
            }
        },
    }
</script>

<template>
    <div class="review shadow-m">
        <div class="review__header">
            <h3 class="author__title">
                {{ review.author }}
            </h3>
        </div>
    </div>
</template>

<style lang="scss" scoped>
    .review {
        display: flex;
        flex-direction: column;

        &__header {
            padding: 5px;
        }
    }

</style>