<script>
import { defineComponent } from 'vue'
import { Bar } from 'vue3-chart-v2'

export default defineComponent({
  name: 'bar',
  extends: Bar,
  mounted () {
    // Overwriting base render method with actual data.
    this.renderChart({
      labels: ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F'],
      datasets: [
        {
          backgroundColor: 'red',
          data: [1, 2, 10, 20, 0, 0, 0, 0, 0, 0, 0]
        }
      ]
    })
  }
})
</script>