class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        s1 = (C-A) * (D-B)
        s2 = (G-E) * (H-F)
        if max(A,E) < min(C,G) and max(B,F) < min(D,H):
            cross = (min(C,G) - max(A,E)) * (min(D,H) - max(B,F))
        else:
            cross = 0
        return s1 + s2 - cross
