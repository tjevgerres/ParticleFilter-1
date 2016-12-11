import matplotlib.pyplot as plt
import seaborn as sns

class ParticleFilterVisualization(object):
    def __init__(self, all_states, get_true_obs, particles, y_particle=None, true_state=None):
        self.fig = plt.figure()
        ax = self.fig.add_subplot(1, 1, 1)

        true_obs = [get_true_obs(state) for state in all_states]
        self.env_plt, = ax.plot(all_states, true_obs, lw=5, zorder=1)

        if true_state:
            self.obs_plt, = ax.plot([true_state, true_state],
                                    [y_particle, get_true_obs(true_state)],
                                    '.-', ms=20, zorder=3)
        else:
            self.obs_plt, = ax.plot([all_states[0], all_states[-1]],
                                    [y_particle, y_particle],
                                    '--', lw=3)

        self.particles_plt, = ax.plot(particles, [y_particle] * len(particles),
                                      '.', ms=20, zorder=2, alpha=0.2)

        plt.ylim([0, 80])
        plt.show(block=False)

    def update(self, particles, obs, true_state=None):
        self.particles_plt.set_xdata(particles)

        if true_state:
            self.obs_plt.set_xdata([true_state, true_state])
            self.obs_plt.set_ydata([70, obs])
        else:
            self.obs_plt.set_ydata([obs, obs])

        self.fig.canvas.draw()